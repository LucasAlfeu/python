class Carro:
    def __init__ ( self, modelo, marca ):
        self.__modelo = modelo
        self.__marca = marca
        self.__velocidade = 0
        self.__ligado = False
    
    def ligar(self):
        self.set_esta_ligado(True)
        print("O motor do carro {} está ligado".format(self.__modelo))

    def acelerar(self, valor):
        self.__velocidade += valor
        print("O carro está a {} Km/h".format(self.__velocidade))

    def desacelerar(self, valor):
        self.__velocidade -= valor
        if (self.__velocidade == 0):
            print("O carro parou")
        else:
            print("O carro está a {} Km/h".format(self.__velocidade))

    def parar(self):
        self.set_parada_brusca()
        print("Cuidado, você parou o carro bruscamente")

    def desligar(self):
        self.set_esta_desligado(False)
        print("O carro está desligado")

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def motor_esta_ligado(self):
        return self.__ligado

    @property
    def modelo(self):
        return self.__modelo

    @property
    def marca(self):
        return self.__marca

    def set_esta_desligado(self, opacao):
        self.__ligado = opacao

    def set_esta_ligado(self, opcao):
        self.__ligado = opcao

    def set_parada_brusca(self):
        self.__velocidade = 0