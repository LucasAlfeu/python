class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1  
    
    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
       return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
       return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.temporadas} temporadas - Likes: {self.likes}'

class Playlits:                                                          #tendo list como herança, nós herdamos tudos de list inclusive transformamos a classe em iteravel
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas
    
    def __getitem__(self, item):        #esse método transforma a classe em iterável sem passar list como herança
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
tmep = Filme('todo mundo em pânico', 1999, 100)
atlanta = Serie("atlanta", 2018, 2)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlits('fim de semana', filmes_e_series)

print(f'O tamanho do playlist: {playlist_fim_de_semana.tamanho}')

for programa in playlist_fim_de_semana:
    print(programa)
    