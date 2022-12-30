usuarios = {1, 5, 76, 34, 52, 13, 17}
len(usuarios) # 7

usuarios.add(765)       # Adicionando elementos no conjunto
len(usuarios) # 8

usuarios_imutaveis = frozenset(usuarios)     # Transforma o conjunto em imutável, congela ele