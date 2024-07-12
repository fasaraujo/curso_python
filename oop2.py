# ORIENTAÇÃO A OBJETO
# CONCEITOS (CLASSE) - > Molde do objeto
#           (ATRIBUTO) -> Variaveis / Parametros passados
#           (MÉTODO) -> fUNÇÕES QUE MANIPULAM e PROCESSAM O OBJETO
#          def __init__(self, x,y): -> Método construtor do objeto em Pyrhon.
# EX: OBJETO
# Classe Fracao  // atributos (numerador/denominador) // métodos (soma, subtrai,multiplica, inverte)

class Fracao:    
    def __init__(self, num, den):   
        print('Instânciando o objeto..: {}'.format(self))
        self.__numerador = num
        self.__denominador = den
        if (self.__denominador == 0):
            self.__denominador = 1
        else:
            self.__denominador = den
    @property
    def inverte(self):
        return self.__denomiandor,self.__numerador

    @property
    def verfr(self):
        return print(self.__numerador,self.__denominador)

fr1 = Fracao(3,4)
fr1.verfr
fr1.inverte



