# Modelagem objeto Cabo
# 12fo
# 25kg/km
# 25mm diametro externo
# tração maxima 50kgF
# Flecha 2,5%

class Cabo:
    def __init__(self, fos, peso, diametro, tracaomax, flecha): 
        self.fos = fos
        self.peso = peso
        self.diametro = diametro
        self.tracaomax = tracaomax
        self.flecha = flecha 
        
fo12 = Cabo(12,85,40,50,2.5)
fo06 = Cabo(6,50,35,40,2.0)

def mostrafibra(self):
    print('Cabo de {} fibras peso de {} Kg/Km, diametro {} mm, Tração Max {} KgF, Flecha {} %'.format(self.fos, self.peso, self.diametro,self.tracaomax, self.flecha))

mostrafibra(fo12)
mostrafibra(fo06)

class Retangulo:

   def __init__(self, x, y):
    self.__x = x
    self.__y = y
    self.__area = x * y

   def pegaarea(self):
    return self.__area 

teste = Retangulo(7,7)
x = teste.pegaarea()
print(x)

listaTetas = [0.92,0.86,0.80,0.90,0.87,0.94,0.67]
pos = 0

def bCap():
  corrige = 0.94
  return corrige

arnacorrige = bCap()

for teta in listaTetas:

  if (teta >= 0.92):
      print('FP Medido -> {:.2f} na posição -> {} - Corrigir para -> NÃO CORRIGIR'.format(teta,pos))
  else:
      print('FP Medido -> {:.2f} na posição -> {} - Corrigir para -> {:.2f}'.format(teta,pos,arnacorrige))
  pos +=1


