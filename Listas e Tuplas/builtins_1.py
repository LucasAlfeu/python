idades = [15, 87, 65, 56, 32, 49, 37]

# for i in range(len(idades)):
#     print(f'{i}: {idades[i]}')

enumerate(idades) # Cria uma enumeração para uma lista quando pedido / Gera a enumeração a medida do necessário

print(list(enumerate(idades))) # [(0, 15), (1, 87), (2, 65), (3, 56), (4, 32), (5, 49), (6, 37)]

for valor in enumerate(idades): 
    pass #print(valor)

for indice, idade in enumerate(idades): # Podemos desempacotar as tuplas no for
    print(indice, '=>', idade)

for _, idade in enumerate(idades): # Desempacotado, quando queremos um valor só podemos usar o undeline para isso
    print(idade)