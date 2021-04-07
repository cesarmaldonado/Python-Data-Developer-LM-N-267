import pprint
import json

perro = dict(nombre = 'Rocco',
             tipo = 'perro',
             raza = 'labrador')

edad = 5

le_gusta = ['comer', 'correr palomas', 'ladrar sin parar']

perro.update(edad = edad, le_gusta = le_gusta)
# perro.update({'le_gusta': le_gusta})

pprint.pprint(perro)

objeto = dict(perro = perro)

with open('perro.json', 'w', encoding= 'utf-8') as archivoJson:
    json.dump(objeto, archivoJson)

with open('perro_lindo.json', 'w', encoding= 'utf-8') as archivoJson:
    json.dump(objeto, archivoJson, indent = 3)