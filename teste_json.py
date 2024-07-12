# Testa gravação de arquivo JSON

import json

arnaLista = [ 
    
    {"nome":"Francisco",
     "cpf":62095749200,
     "dnasc":210777,
     "e-mail":"netservicero@gmail.com"  
    },{
     "nome":"Laiz Sleiman",
     "cpf":3849409934,
     "dnasc":190978,
     "e-mail":"laiz@oi.net.br"  
    },{
     "nome":"Matheus Sleiman",
     "cpf":"NaN",
     "dnasc":230973,
     "e-mail":"matheus@oi.net.br" 
    }
]

ArnaDados  = arnaLista

with open('./dados.json', "w") as file:
    json.dump(ArnaDados,file,indent=2,sort_keys=False)


