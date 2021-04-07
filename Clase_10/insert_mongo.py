from pymongo import MongoClient as MC

cliente = MC('mongodb://localhost:27017')

# estudiante = {'nombre': 'Eduardo', 'apellido': 'Sanz'}
# Insertar un documento
# cliente.universidad.alumnos.insert_one(estudiante)

bd = cliente['universidad']
coleccion = bd['alumnos']
# insertar varios documentos
estudiantes = [{'nombre': 'Javier','apellido': 'Sosa'},
               {'nombre': 'Matias', 'apellido': 'Ferravante'},
               {'nombre': 'Fernando', 'apellido': 'Rubiolo', 'hijos': [{'nombre': 'Javier','apellido': 'Sosa', 'edad': 15},
                                                                       {'nombre': 'Matias', 'apellido': 'Ferravante', 'edad': 1},]}
                ]
coleccion.insert_many(estudiantes)

print('Datos cargados.')