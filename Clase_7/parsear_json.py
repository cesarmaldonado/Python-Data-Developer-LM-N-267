import json
import pprint

with open('perro.json') as archivo:
    objeto = json.load(archivo)
    
pprint.pprint(objeto)
pprint.pprint(objeto.get('perro').get('le_gusta'))