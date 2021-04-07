import pprint

perro = dict(nombre = 'Rocco',
             tipo = 'perro',
             raza = 'labrador')
loro = dict(nombre = 'Carol',
            tipo = 'loro',
            raza = 'cacatúa')
gato = dict(nombre = 'Miu',
            tipo = 'gato',
            raza = 'persa')

mascotas = dict(perro = perro,
                loro = loro,
                gato = gato)



edad = 5

le_gusta = ['comer', 'correr palomas', 'ladrar sin parar']

perro.update(edad = edad, le_gusta = le_gusta)
# perro.update({'le_gusta': le_gusta})

pprint.pprint(perro)

print(perro.get('le_gusta')[0])

amo = dict(nombre = 'Javier', 
           tipo = 'humano', 
           edad = 33,
           le_gusta = ['los fichines', 'salir los sabados', 'el futbol'],
           mascotas = mascotas)

pprint.pprint(amo)

