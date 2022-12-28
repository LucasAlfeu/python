idades = [39, 30, 27, 18]

#idades.append(15)
# idades.remove(30)
# idades.pop()
#idades.extend([26, 45])
#idades.sort()
#idades.insert(0, 33)
print(idades)

# maior_que_trinta = [idade for idade in idades if idade > 30]
# print(maior_que_trinta)

def soma_um(idade):
    return idade + 1

idades_ano_que_vem = [soma_um(idade) for idade in idades]
#print(idades_ano_que_vem)

