meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

# Contando quantas vezes cada palavra aparece

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

from collections import defaultdict

# ----------------------------------------------------------------------------
aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

# ----------------------------------------------------------------------------
aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

from collections import Counter

aparicoes = Counter(meu_texto.split())

print(aparicoes)