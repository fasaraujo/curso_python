# Algoritimo busca binaria

minhalista = [1,3,5,7,9,12,15,40]

def pesquisa_binaria(lista, item):
  baixo = 0
  alto = len(lista) -1
  while (baixo <= alto):
    meio = int((baixo + alto)/2)
    chute = lista[meio]
    if (chute == item):
      return meio 
    if (chute > item):
      alto = meio -1
    else:
      baixo = meio +1
  return

teste = pesquisa_binaria(minhalista,3)

if (teste == 0):
  print('NÃO ENCONTRA')
else:
  print('ENCONTRADO...', teste)
