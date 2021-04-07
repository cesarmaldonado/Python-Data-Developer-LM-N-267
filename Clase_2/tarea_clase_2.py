import csv
from datetime import datetime

def normalizadorFechas(fecha, formato_in, formato_out = "%d-%m-%Y"):
   objeto_fecha = datetime.strptime(fecha, formato_in)
   fecha_normalizada = datetime.strftime(objeto_fecha, formato_out)
   return fecha_normalizada
   
def traductorFecha(fecha):
    meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
    lista = fecha.split(' ')
    mes = lista[2].upper()
    nro_mes= meses.index(mes) + 1
    fecha_aux = lista[0]+ '/'+ str(nro_mes)+ '/'+ lista[4]
    return fecha_aux

archivo_in = open('reclamos.csv', encoding = 'ansi')
archivo_out = open('reclamos_normalizado.csv','w',encoding = 'ansi')
tabla = csv.reader(archivo_in, delimiter = ';')
next(tabla)
archivo_out.write('id_cliente;tx_zona;tx_reclamo;fc_reclamo\n')


for linea in tabla:
    fecha = linea[3]
    
    try: 
        fecha_normalizada = normalizadorFechas(fecha, '%d/%m/%Y')
    except:
        try:
            fecha_normalizada = normalizadorFechas(fecha, '%Y/%m/%d')
        except:
            try:
                fecha_normalizada = normalizadorFechas(fecha, '%m/%d/%Y')
            except:
                try:
                    fecha_normalizada = normalizadorFechas(fecha, '%Y/%d/%m')
                except:
                    try:
                        fecha_normalizada = normalizadorFechas(fecha, '%d-%m-%Y')
                    except:
                        try:
                            fecha_normalizada = normalizadorFechas(fecha, '%Y-%m-%d')
                        except:
                            try:
                                fecha_normalizada = normalizadorFechas(fecha, '%m-%d-%Y')
                            except:
                                try:
                                    fecha_normalizada = normalizadorFechas(fecha, '%Y-%d-%m')
                                except:
                                    try:
                                        fecha_normalizada = normalizadorFechas(fecha, '%d/%m/%y')
                                    except:
                                        try: 
                                            fecha_normalizada = normalizadorFechas(traductorFecha(fecha), '%d/%m/%Y')
                                        except:
                                            archivo_out.write(linea[0]+ ';'+ linea[1]+ ';'+ linea[2]+ ';'+ 'fecha mal escrita'+ '\n')
    archivo_out.write(linea[0]+ ';'+ linea[1]+ ';'+ linea[2]+ ';'+ fecha_normalizada + '\n')
archivo_in.close()
archivo_out.close() 