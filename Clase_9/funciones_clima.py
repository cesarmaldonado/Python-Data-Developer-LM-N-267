import json
import requests

def obtenerLng(key_geo,ciudad_cod):
    url = 'https://api.opencagedata.com/geocode/v1/json?q='+ ciudad_cod + '&language=es&key=' + key_geo
    objeto = json.loads(requests.get(url).text)
    lng = objeto['results'][0]['geometry']['lng']
    return lng

def obtenerLat(key_geo,ciudad_cod):
    url = 'https://api.opencagedata.com/geocode/v1/json?q='+ ciudad_cod + '&language=es&key=' + key_geo
    objeto = json.loads(requests.get(url).text)
    lat = objeto['results'][0]['geometry']['lat']
    return lat

def clima(key_clima, lat, lng):
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) +'&lon='+ str(lng) + '&units=metric&lang=es&appid=' + key_clima
    objeto = json.loads(requests.get(url).text)
    return objeto

def ciudadcodificada(ciudad):
    ciudad_cod = requests.utils.quote(ciudad[0]) + ', Argentina'
    return ciudad_cod

def keys():
    archivo_key = open('keys.csv', encoding= 'utf-8')
    for linea in archivo_key:
        linea = linea.replace('\n', '')
        linea = linea.split(',')
        if linea[0] == 'key_clima': key_clima = linea[1]
        else: key_geo = linea[1]
    return key_clima, key_geo