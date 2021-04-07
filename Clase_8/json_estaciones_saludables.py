import requests
import json
import pprint
import csv

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/vicejefatura-de-gobierno/estaciones-saludables/estaciones-saludables.geojson'
contenido = requests.get(url).text
objeto = json.loads(contenido)


archivo_out = open('estaciones_saludables.csv','w',encoding = 'utf-8')
archivo_out.write("latitude,longitude,name,label\n")


for i in range(len(objeto['features'])):
    latitude = (objeto["features"][i]["geometry"]["coordinates"][1])
    longitude = (objeto["features"][i]["geometry"]["coordinates"][1])
    name = (objeto["features"][i]["properties"]["nombre"])
    label = (objeto["features"][i]["properties"]["ubicacion"])
    archivo_out.write(str(latitude) + ',' + str(longitude) + ',' + name + ',' + label + '\n')


archivo_out.close() 
