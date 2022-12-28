idades = [15, 87, 65, 56, 32, 49, 37]
# print(idades)
# print(sorted(idades)) # o sorted devolve uma lista
# print(sorted(idades, reverse=True))
idades.sort() # ordenar atribuindo e mudando a lista original
reversed(idades) # devolve um iterador e não uma lista

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
            
        return self._codigo == outro._codigo and self._saldo == outro._saldo
    
    def __lt__(self, outro):
        return self._saldo < outro._saldo
    
    def deposita(self, valor):
        self._saldo += valor
    
    def __str__(self):
        return f'[>>Código {self._codigo}, Saldo {self._saldo}<<]'

conta_guilherme = ContaSalario(17)
conta_guilherme.deposita(500)

conta_daniela = ContaSalario(3)
conta_daniela.deposita(1000)

conta_paulo = ContaSalario(133)
conta_paulo.deposita(510)

contas = [conta_paulo, conta_daniela, conta_guilherme]

# Para ordenar classes precisamos fazer da seguinte maneira

def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
    pass

# Esse primeiro método é eficaz mas acessamos um atributo privado :( vejamos outro método

from operator import attrgetter

for conta in sorted(contas, key=attrgetter('_saldo')):
    pass

# Ou então podemos atribuir o método __lt__ para fazer essa comparação sem acessar nenhum atributo privado fora da classe

for conta in sorted(contas, reverse=True):
    print(conta)