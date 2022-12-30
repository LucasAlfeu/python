aparicoes = {
    'Guilherme': 1,
    'cachorro': 2,
    'nome': 2,
    'vindo': 1
}

aparicoes['Guilherme'] # 1

# Podemos iniciar um dicionário da seguinte forma também:

repeticoes = dict(Guilherme = 2, cachorro = 1) # {'Guilherme': 2, 'cachorro': 1}

# Adicionando elementos no dicionário

aparicoes['Carlos'] = 1 # {'Guilherme': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1, 'Carlos': 1}

# Reatribuindo um valor 

aparicoes['Carlos'] = 2 # {'Guilherme': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1, 'Carlos': 2}

# Remover 

del aparicoes['Carlos'] # {'Guilherme': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1}
print(aparicoes)

'cachorro' in aparicoes