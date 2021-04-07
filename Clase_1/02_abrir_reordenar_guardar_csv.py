# Abrir y trabjar con un archivo csv

archivo_in = open('subtes.csv' , encoding = 'utf-8')
archivo_out = open('subtes_mod.csv' , 'w', encoding = 'utf-8')
for linea in archivo_in:
    linea = linea.replace('\n', '')
    linea = linea.split(',')
    # print(linea[2], linea[1], linea[0])
    archivo_out.write(linea[2] + ',' + linea[1] + ',' + linea[0] + '\n')    


archivo_in.close()
archivo_out.close()
