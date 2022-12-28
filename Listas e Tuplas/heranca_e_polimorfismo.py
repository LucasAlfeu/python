from abc import ABCMeta, abstractclassmethod

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor
    
    @abstractclassmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f'>> Código {self._codigo} Saldo {self._saldo} <<'

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaIvestimento(Conta):
    pass

conta16 = ContaCorrente(16)
conta16.deposita(1000)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)

# Temos os benefícios do Poliformismo em um iterável
contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()
    print(conta)