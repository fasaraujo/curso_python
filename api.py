# Testa a API do compras.gov.br
# estrutura de acesso ['Nivel1']['Nivel2'][indice]['campo']

import requests

def tela():
  print('#########################')
  print('# Comunicando com a API #')
  print('#########################')
  
endpoint = "http://compras.dados.gov.br/fornecedores/v1/fornecedores.json?id_municipio=90514"

tela()

arnaRespostaServer = requests.get(endpoint)

if (arnaRespostaServer.status_code != 200):
  print()
  print('Falha na comunicação com a API')
else:
  arnaColeta = arnaRespostaServer.json()
  
indice = 0
for i in arnaColeta["_embedded"]['fornecedores']:
  print('--------------------------------------------------')
  print('Nome..:', arnaColeta["_embedded"]['fornecedores'][indice]['nome'])
  print('Cnpj..:', arnaColeta["_embedded"]['fornecedores'][indice]['cnpj'])
  print('Habilitado para Licitar..:', arnaColeta["_embedded"]['fornecedores'][indice]['habilitado_licitar'])
  print('--------------------------------------------------')
  indice +=1

print('Total de Empresas..: {}'.format(indice))
  
  