# Fixação dos conceitos de orientação a objetos no
# python.

# Define classe perfil (classe principal)
# Conceitos -> Objeto -> Classe -> Atributos -> Métodos
# Herança / Polimorfismo, enacpsulamento, getter and setter

class Perfil():
    def __init__(self, nome, idade, status_civil, cidade, uf, likes):
        self.nome = nome.title()
        self.idade = idade
        self.status_civil = status_civil  
        self._cidade = cidade ## encapsulo
        self._uf = uf ## encapsulo
        self._likes = 0
       
    def likes(self):
        return self._likes
    
    def darlikes(self):
        self._likes += 1

    def dislike(self):
        self._likes -= 1
        if (self._likes < 0):
            self._likes = 0
        else:
            self._likes = self._likes

    @property
    def cidade(self):
        return self._cidade
    
    @property
    def uf(self):
        return self._uf

    def mostraPerfil(self):
        print('Olá eu sou {} tenho {} sou {} moro {} estado {} - Likes: {}'.format(self.nome,self.idade,self.status_civil,self.cidade,self.uf,self.likes))   

class Hobby(Perfil):  # Herda atributos e métodos da classe Perfil
    pass


# Criar rotina de criação de perfil na rede
# Instância objetos
Francisco = Perfil("Francisco",45,"solteiro","Campo Grande","ms",0)
Laiz = Perfil("Laiz",44,"solteira","Campo Grande","ms",0)

#Francisco.darlikes()
#Francisco.mostraPerfil()



