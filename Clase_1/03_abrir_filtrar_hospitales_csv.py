#  Abrir archivo Hospitales.csv de data.buenosaires.com.gob
#  Filtrar en un archivo de salida latitud, longitud, nombre y dirección
import csv
archivo_in = open('hospitales.csv', encoding= 'utf-8')
archivo_out = open('hospitales_filtrado.csv', 'w', encoding= 'utf-8')
lectura = csv.reader(archivo_in)
next(lectura)
archivo_out.write('latuitude,longitude,name,label\n')
for linea in lectura:
    # print(linea[1], linea[0], linea[4], linea[8])
    archivo_out.write(linea[1] + ',' + linea[0] + ',' + linea[8] + ',' + linea[4]+ '\n')    


archivo_in.close()
archivo_out.close()

