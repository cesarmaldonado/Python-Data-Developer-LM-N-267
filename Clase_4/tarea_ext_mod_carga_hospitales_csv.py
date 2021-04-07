import requests
import csv
from io import StringIO
import mysql.connector

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.csv'
respuesta = requests.get(url)
contenido = respuesta.text
archivo_str = StringIO(contenido)

archivo_in =  csv.reader(archivo_str)
archivo_out = open('Hospitales_mod.csv', 'w', encoding = 'utf-8')
next(archivo_in)

for lista in archivo_in:
    lista_aux = lista[0].replace('POINT (', '')
    lista_aux2 = lista_aux.replace(')', '')
    lista_mod = lista_aux2.split(' ')
    archivo = archivo_out.write(lista_mod[1]+ ','+ lista_mod[0]+ ','+ lista[2]+ ','+ lista[5]+ ' '+ lista[6]+ '\n')
 
conexion = mysql.connector.connect(
                host = 'cloud.eant.tech',
                database = 'pdp_base001',
                user = 'pdp_usuario001',
                password = 'eantpass')
        
cursor = conexion.cursor()
archivo_out = open('Hospitales_mod.csv', 'r', encoding = 'utf-8')
hospitales_csv = csv.reader(archivo_out)
next(hospitales_csv)
for lista in hospitales_csv:
    sql = "INSERT INTO hospitales (latitude, longitude, name, label) VALUES ('"+lista[0]+"', '"+lista[1]+"', '"+lista[2]+"', '"+lista[3]+"')"
    cursor.execute(sql)
    conexion.commit()
    
cursor.close()
conexion.close()
archivo_out.close()