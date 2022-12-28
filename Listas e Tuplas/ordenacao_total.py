from operator import attrgetter
from functools import total_ordering


@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        else:
            return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[>>Código {self._codigo}, Saldo {self._saldo}<<]'


conta_guilherme = ContaSalario(1700)
conta_guilherme.deposita(500)

conta_daniela = ContaSalario(3)
conta_daniela.deposita(1000)

conta_paulo = ContaSalario(133)
conta_paulo.deposita(500)

contas = [conta_paulo, conta_daniela, conta_guilherme]

# Podemos ordenar por mais de um atributo, basta passa-lo no attrgetter

for conta in sorted(contas, key=attrgetter('_saldo', '_codigo')):
    pass

    # Mas ainda sim acessamos um atributo privado.
    # Podemos alterar o método __lt__ da seguinte forma

    # def __lt__(self, outro):
    #     if self._saldo != outro._saldo:
    #         return self._saldo < outro._saldo
    #     else:
    #         return self._codigo < outro._codigo

for conta in sorted(contas):
    print(conta)

    # Para fazer a ordenação com os operadores <= ou >= precisamos importar o total_ordering do functools e mostra que a classe terá o decorator de @total_ordering
    # para isso precisamos ter implementado os metodos __lt__ e o __eq__

    # from functools import total_ordering

    # @total_ordering
    # class ContaSalario:
    #     def __init__(self, codigo):
    #         self._codigo = codigo
    #         self._saldo = 0
