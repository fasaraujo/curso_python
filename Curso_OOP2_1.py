
# User esta classe para Herança

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def darLikes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

# FIM CLASSE MÃE - SERÁ USADA COMO HERANÇA
        
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
   
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

Vingadores = Filme('Vingadores - Guerra Infinita',2018,160)
Atlanta = Serie('Atlanta', 2018,2)

Vingadores.darLikes()
Vingadores.darLikes()
Atlanta.darLikes()

print('Filme: {} Ano {} Duração {} Likes: {}'.format(Vingadores.nome,Vingadores.ano,Vingadores.duracao,Vingadores.likes))
print('Filme: {} Ano {} Temporada {} Likes: {}'.format(Atlanta.nome,Atlanta.ano,Atlanta.temporadas,Atlanta.likes))

