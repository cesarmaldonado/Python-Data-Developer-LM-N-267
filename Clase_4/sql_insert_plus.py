import mysql.connector

conexion = mysql.connector.connect(
                host = 'cloud.eant.tech',
                database = 'pdp_base001',
                user = 'pdp_usuario001',
                password = 'eantpass')

cursor = conexion.cursor()#inicio el cursor para poder trabajar 

ingresar = True

while ingresar:
    dni = input("Ingrese el dni 'enter' para continuar: ")
    sql = "SELECT dni FROM alumnos WHERE dni LIKE '"+dni+"'"
    cursor.execute(sql)
    dni_cargado = 0
    for dnituple in cursor:
        dni_cargado = dnituple[0]
        
    
    if int(dni)== dni_cargado: 
        print('Alumno ya cargado')
        ingresar = False     
    else:
        nombre = input("Ingrese el nombre del alumno, 'enter' para continuar: ")
        apellido = input("Ingrese el apellido, 'enter' para continuar: ")
        email = input("Ingrese el email, 'enter' para continuar: ")
        fecha_nac = input("Ingrese la fecha de nacimiento (AAAA-MM-DD) o 'enter' para continuar: ")
        sql = "INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac) VALUES ('"+nombre+"', '"+apellido+"', '"+dni+"', '"+email+"', '"+fecha_nac+"' )"
        cursor.execute(sql)
        salida = input('Desea ingresar otro alumno? (S/N): ').upper()
        if salida == 'N' : ingresar = False
    

conexion.commit()# guarda todos los comandos
  
cursor.close()
conexion.close()
