import mysql.connector

conexion = mysql.connector.connect(
                host = 'cloud.eant.tech',
                database = 'pdp_base001',
                user = 'pdp_usuario001',
                password = 'eantpass')

cursor = conexion.cursor()
sql = 'SELECT * FROM alumnos'

cursor.execute(sql)

for alumno in cursor:
    print(alumno)
    
cursor.close()
conexion.close()
