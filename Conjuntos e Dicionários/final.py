texto1 = """
Por fim, vamos colocar tudo isso em prática para vermos algum exemplo diferente? Então o que eu queria fazer agora não é um contador de palavras, eu fazer um contador de letras para vermos uma coisa interessante que acontece na língua portuguesa e em outras línguas, para ser sincero, também. Então eu vou criar aqui uma nova sessão que é "#Testando o uso de diversas coleções".
Então o que vamos fazer é o seguinte: vamos pegar dois textos, por exemplo eu posso entrar no blog da Alura e pegar textos do blog da Alura. Eu posso pegar um texto que está falando sobre expressões regulares e posso pegar um outro texto de outro assunto, só para não termos dois assuntos similares. Vou pegar um o outro assunto, temos um de programação e um aqui que é de negócios: B2C, B2B, coisas do gênero. Então dois assuntos distintos, um de programação e um não de programação.
"""

texto2 = """
Mas quando tem uma palavra, por exemplo "guilherme", e eu fizer um for x in "guilherme":, cada um dos elementos x é o que? É uma das letras. Então em um texto, você pode considerar, entre aspas, que uma string é como se funcionasse como uma lista ou um iterável de caracteres. Um texto string no Python é um iterável de caracteres, você pode pensar dessa maneira. E já que isso é verdade, aqui da maneira que eu estou trabalhando, então eu poderia criar um contador em cima do texto1.
Counter(texto1)
Vamos criar um contador em cima do texto1? Olha aqui: quantas vezes cada letra "A"pareceu. Maiúsculo e minúsculo, então texto1.lower(). Então quantas vezes cada letra "A"pareceu, em minúsculo, já no minúsculo. Então as aparições estão aí. Agora eu tenho a contagem de cada letra, eu queria saber o quão frequente apareceu a letra "A", o caractere "A", o quão frequente apareceu o caractere "E", o quão frequente apareceu o caractere hífen, o caractere quebra de linha. O caractere quebra de linha eu não estou interessado pessoalmente, mas vamos fazer para todos, vamos trabalhar para todos de uma maneira uniforme.
"""

from collections import Counter
def analisa_frequencia_de_letras(texto): 
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(f'{caractere} => {proporcao * 100 :.2f}%')

analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)