class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property                       # transforma o método em uma propriedade
    def nome(self):
        return self.__nome.title()

    @nome.setter                    # altea o nome como um seter mas em propriedade e não como métdodo
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome