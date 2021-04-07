import requests
import pprint
import json
import csv


key_clima = '02ddb357144e42bbf70729a19c51d4d1'
key_geo = '5f592ec0596c48b19eafb32a3ad6bd75'

archivo_in = open('sucursales_sol_360.csv')
log_error = open('sol360_log_error.txt', 'w')

for ciudad in archivo_in:
    ciudad = ciudad.split(';')
    ciudad_cod = requests.utils.quote(ciudad[0]) + ', Argentina'
    url = 'https://api.opencagedata.com/geocode/v1/json?q='+ ciudad_cod + '&language=es&key=' + key_geo
    objeto = json.loads(requests.get(url).text)
    lat = objeto['results'][0]['geometry']['lat']
    lng = objeto['results'][0]['geometry']['lng']
   
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) +'&lon='+ str(lng) + '&units=metric&lang=es&appid=' + key_clima
    objeto = json.loads(requests.get(url).text)
    if objeto.get('weather')== None:
        log_error.write(ciudad[0] + ' no encontrada \n')
    else:
        print(ciudad[0], ',', ciudad[1])
        print('Descripción: ', '\t', objeto.get('weather')[0]['description'])
        print('Temperatura: ', '\t', objeto.get('main')['temp'], ' °C')
        print('Humedad: ', '\t\t', objeto.get('main')['humidity'], ' %\n')

log_error.close()