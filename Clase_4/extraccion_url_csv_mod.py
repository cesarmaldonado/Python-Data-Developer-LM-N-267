import requests
import csv
from io import StringIO

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSHeFztDDRirQZmt0FdI6Yu1SzAxVn0sLKa0ITXlhgHNLwsTp2TuPKACjEYOCebLWwBZoR05Vz6M-Wo/pub?gid=1561509104&single=true&output=csv'
respuesta = requests.get(url)
contenido = respuesta.text
archivo_str = StringIO(contenido)# le da formato al str

objeto_csv = csv.reader(archivo_str)

archivo = open('peliculas_mod_google.csv', 'w')
for linea in objeto_csv:
   archivo.write(linea[0]+ ',' + linea[2]+ ','+ linea[1] + '\n')
archivo.close()