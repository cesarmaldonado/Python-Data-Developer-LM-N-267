import mysql.connector

conexion = mysql.connector.connect(
                host = 'cloud.eant.tech',
                database = 'pdp_base001',
                user = 'pdp_usuario001',
                password = 'eantpass')

cursor = conexion.cursor()
sql = '''INSERT INTO alumnos (nombre, apellido, dni, email, fecha_nac)
VALUES ("Matias", "Ferravante", "34568975", "matiasferravante123@ferravante.com", "1995-06-19")'''

cursor.execute(sql)
conexion.commit()

    
cursor.close()
conexion.close()
