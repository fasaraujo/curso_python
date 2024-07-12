# teste da API viaCep.com.br

import requests
import json

def tela():
  print()
  print('     ------------------------')
  print('     - Comunicando com a API-')
  print('     ------------------------')
  
arnaContinua = 'S'

while (arnaContinua == 'S'):
  
  arnaPegaCep = str(input('Digite o CEP..:').strip())
  arnaEndPoint = 'https://viacep.com.br/ws/{}/json/'.format(arnaPegaCep)
  arnaPegaRespostaServer = requests.get(arnaEndPoint)

  tela()
  
  if (arnaPegaRespostaServer.status_code != 200):
    print('Falha na comunicação com a API')
  else:
    r = arnaPegaRespostaServer.json()
    print('------------------------------------')
    #print('Status Code.:{}'.format(arnaPegaRespostaServer.status_code))
    #print('Hearders..: {}\n'.format(arnaPegaRespostaServer.headers))
  #print(r.keys())
  # print(        'Pesquisando..: {}'.format(time.sleep(5)))
  # print('     Comunicando com a API ..')
    print('------------------------------------')
    print('CEP..:',r['cep'])
    print('LOGRADOURO..:',r['logradouro'])
    print('COMPLEMENTO..:',r['complemento'])
    print('BAIRRO..:',r['bairro'])
    print('LOCALIDADE..:',r['localidade'])
    print('UF..:',r['uf'])
    print('------------------------------------')

  arnaContinua = str(input('Deseja continua a pesquisa [S/N].:').upper())

