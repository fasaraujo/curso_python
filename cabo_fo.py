import math

# (p) = Peso do cabo em Kg/m
# (h) = Componente horizontal do vento em Kg/m
# (r) = Carga Resultante 

# Caracteristicas cabo de fibra optica 12.fo AS-80 c/ núcleo seco
# Massa nominnal (kg/km) -> peso do cabo = (81)
# Diametro externo (mm) AS-80 12f.o  -> (9.3) c/ núcleo seco

def vao():
  arnapegavao = 0
  arnasomavao = 0
  arnacubo = 0
  arnasoma_cubo = 0
  arna_again = 'S'

  while arna_again == 'S':
    arnapegavao = float(input("informe o vão em metros..:"))
    arna_again = str(input("Continua [S/N]")).upper()
    arnasomavao += arnapegavao
    arnacubo += (arnapegavao **3)
    arnasoma_cubo += arnacubo
    arnacubo = 0
  else:
      #print("total do vao acumulado..: {:.2f}".format(arnasomavao))
      #print("Vao regulador ..: {:.2f}".format(math.sqrt(arnasoma_cubo/arnasomavao)))
    vregulador = math.sqrt(arnasoma_cubo/arnasomavao)
    return(vregulador)

def telaparam():
    print('-'*50)
    return 

telaparam()
pesoCabo = float(input('Informe o Peso do Cabo [Kg/Km].:'))
diaExternoCabo = float(input('Informe o Diametro Externo do cabo [mm].:'))
hvento = float(input('Velocidade do Vento [m/s].:'))
flecha = float(input('Informe a Flecha [%].:'))
telaparam()

hvento = 20 
telaparam()
vr = vao()
diaExternoCabo = (diaExternoCabo/1000)
comphorizontal = (hvento*diaExternoCabo)
flecha = (flecha*vr)/100
pesoCabo = (pesoCabo/1000)

cr = math.sqrt(math.pow(comphorizontal,2)+math.pow(pesoCabo,2))

# Tracao = R*L2 / 8.f

tracao = (cr*(vr**2))/(8*flecha)
telaparam()
print('Esforço Mecanico no trecho[kgf].:{:.1f}'.format(tracao))
telaparam()
