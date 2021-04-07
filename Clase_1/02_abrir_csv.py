# Abrir y trabjar con un archivo csv
archivo = open('subtes.csv' , encoding = 'utf-8')
for linea in archivo:
    linea = linea.replace('\n', '')
    linea = linea.split(',')
    print(linea[2])    
    
archivo.close()
