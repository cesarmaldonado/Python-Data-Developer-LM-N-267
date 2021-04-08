from pymongo import MongoClient as MC
import json
import requests

cliente = MC('mongodb://localhost:27017')

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/vicejefatura-de-gobierno/estaciones-saludables/estaciones-saludables.geojson'
contenido = requests.get(url).text
objeto = json.loads(contenido)['features']


bd = cliente['salud']
coleccion = bd['estaciones saludables']
coleccion.insert_many(objeto)

print('Datos cargados.')