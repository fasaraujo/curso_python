
import requests

alvo = 'https://valor.globo.com/'

conecta = requests.get(alvo)
pega_status = conecta.status_code
pega_header = conecta.headers

if (pega_status != 200):
  print('FALHA NA CONEXÃO')
else:
  print('CONEXÃO OK')
  print(pega_status)
  print(pega_header)

  
