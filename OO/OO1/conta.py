class Conta:

    def __init__(self, numero, titular, saldo, limite):
        ("Construindo objeto ...")
        self.__numero = numero          # __ um aviso antes do atributo que não deve acessar esses atributos poi sé privado
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(" Saldo {} do titular {}". format(self.__saldo, self.__titular))
    
    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar
    
    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))
    
    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):                # get somente retorna as informações, just read
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def set_limite(self, novo_limite):          # set nunca retorna nada somente muda algo
        self.__limite = novo_limite

    @staticmethod                        # permite chamar o metodo sem ter nenhuma objeto criado
    def codigo_banco():
        return "001"