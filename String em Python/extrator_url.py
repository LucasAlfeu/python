import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    # Limpera e validação de URL
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)          # Match verifica se a string inteira bate com o nosso padrão
        if not match:
            raise ValueError("A URL não é válida")


    # Métodos sobre a URL       
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base
    
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[(indice_interrogacao + 1):]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def cambio_de_moedas(self):
        VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
        moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
        moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
        quantidade = int(extrator_url.get_valor_parametro("quantidade"))
        if (moeda_origem == 'real' and moeda_destino == 'dolar'):
            cambio = quantidade / VALOR_DOLAR
            return print(f'O valor do cambio é {round(cambio, 2)} reais') 
        else:
            cambio = quantidade * VALOR_DOLAR
            return print(f'O valor do cambio é {round(cambio, 2)} dólares') 

    # Métodos especiais        
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base
    
    def __eq__(self, other):
        return self.url == other.url

extrator_url = ExtratorURL("https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
print(f'O tamanho da URL: {len(extrator_url)}')

valor_quantidade = extrator_url.get_valor_parametro('quantidade')

extrator_url.cambio_de_moedas()