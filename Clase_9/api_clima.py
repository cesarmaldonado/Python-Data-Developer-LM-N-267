import requests
import pprint
import json
import csv


key = '02ddb357144e42bbf70729a19c51d4d1'

archivo_in = open('sucursales_sol_360.csv')
log_error = open('sol360_log_error.txt', 'w')

for ciudad in archivo_in:
    ciudad = ciudad.split(';')
    ciudad_cod = requests.utils.quote(ciudad[0])
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad[0] +'&appid='+ key+ '&lang=es'
    objeto = json.loads(requests.get(url).text)
    if objeto.get('weather')== None:
        log_error.write(ciudad[0] + ' no encontrada \n')
    else:
        print(ciudad[0]+ '---'+ objeto.get('weather')[0]['description'])
        

log_error.close()