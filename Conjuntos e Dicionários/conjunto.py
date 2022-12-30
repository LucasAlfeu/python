alunos = [13, 15, 56, 24, 42, 23, 43 ,56]

conjunto = set(alunos)  # {42, 43, 13, 15, 23, 56, 24}

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

usuarios_data_science | usuarios_machine_learning      # União de Conjuntos --> {42, 43, 13, 15, 23, 56}

usuarios_data_science & usuarios_machine_learning      # Mostra os elementos que existm no dois conjuntos --> {56, 23}

usuarios_data_science - usuarios_machine_learning      # Mostra somente os elementos que não fazem intersecção com o outro conjunto ---> {43, 15}

usuarios_data_science ^ usuarios_machine_learning       # Mostra todos os elemento que não fazem parte da intersecção  ---> {42, 43, 13, 15}