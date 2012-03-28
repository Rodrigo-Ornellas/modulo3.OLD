#coding: utf-8

''' >> apenas como comentario
[
  {
    "pk": 1, 
    "model": "entrega.cliente", 
    "fields": {
      "ramal": "",      
      "complemento": "", 
      "nome": "Chico Anisio", 
      "fone": "(11) 6666-0000",
      "logradouro": "Deus nos ajude",       
      "numero": 1234,
      "obs": "",       
      "email": ""
    }
  } 
]
'''

LOGRADOUROS = ['Rua Fidalga', 'Rua Girassol', 'Rua Harmonia']

registros = []
from random import randint, choice
for i in range(20):
    campos = dict(ramal='', complemento='', obs='', email='', 
        nome = 'Cliente #%04d' % i, 
        fone = '%4d-%04d' % (randint(2000,4999), randint(0,9999)),
        numero = i + 2000,
        logradouro = choice(LOGRADOUROS))
    reg = dict(pk=i, model='entrega.cliente', fields=campos)
    registros.append(reg)
    
import json
with open('clientela.json', 'wb') as saida:
    json.dump(registros, saida, indent=2)
