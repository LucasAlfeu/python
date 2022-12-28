class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'>> Código {self.codigo} Saldo {self.saldo} <<'

gui = ContaCorrente(15)
dani = ContaCorrente(47586)
gui.deposita(200)
dani.deposita(300)

contas = [gui, dani]

for conta in contas:
    print(conta)