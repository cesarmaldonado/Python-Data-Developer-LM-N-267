edad = {'Jorge': 33, 'Ana': 32}
edades = dict(Jorge=33, Ana=32)

edades['Jorge']

for persona in edades:
    print(persona, ':', edades[persona])
    
# Métodos mas usados
edades.get('Gonzalo', 'Esa persona no está')

edades.update({'Ana': 38})
edades.update(Gonzalo = 49)