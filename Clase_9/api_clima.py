import funciones_clima as fc


archivo_in = open('sucursales_sol_360.csv')
 
log_error = open('sol360_log_error.txt', 'w')

key_clima, key_geo = fc.keys() 

for ciudad in archivo_in:
    ciudad = ciudad.split(';')
    ciudad_cod = fc.ciudadcodificada(ciudad)   
    lat = fc.obtenerLat(key_geo, ciudad_cod)    
    lng = fc.obtenerLng(key_geo, ciudad_cod)    
    clima = fc.clima(key_clima, lat, lng)
    
    if clima.get('weather')== None:
        log_error.write(ciudad[0] + ' no encontrada \n')
    else:
        print(ciudad[0], ',', ciudad[1])
        print('Descripción: ', '\t', clima.get('weather')[0]['description'])
        print('Temperatura: ', '\t', clima.get('main')['temp'], ' °C')
        print('Humedad: ', '\t\t', clima.get('main')['humidity'], ' %\n')

log_error.close()