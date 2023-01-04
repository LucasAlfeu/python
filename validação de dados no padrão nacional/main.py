from acesso_cep import BuscaEndereco

cep = '25870146'
objeto_cep = BuscaEndereco('01001000')
bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)

