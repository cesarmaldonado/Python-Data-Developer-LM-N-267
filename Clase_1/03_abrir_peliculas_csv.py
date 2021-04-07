# Abrir y trabajar con peliculas.csv

archivo_in = open('peliculas.csv' , encoding = 'utf-8')
archivo_out = open('peliculas_mod.csv' , 'w', encoding = 'utf-8')
for linea in archivo_in:
    linea = linea.replace('\n', '')
    linea = linea.replace('"', '')
    linea = linea.split(',')
    # linea[3] = linea[3].strip('"')    
    # linea[5] = linea[5].strip('"')
    print(linea[0], linea[3], linea[4], linea[5])
    archivo_out.write(linea[0] + ',' + linea[3] + ',' + linea[4] + ',' + linea[5] + '\n')    


archivo_in.close()
archivo_out.close()
