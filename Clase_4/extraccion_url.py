import requests

url = 'https://eant.tech/cursos/recursos/frutas.txt'
respuesta = requests.get(url)

print('codigo de respuesta: ', respuesta.status_code)
print('url: ', respuesta.url)
print('contenido "crudo": ', respuesta.content)
print('como texto: ', respuesta.text)
print('codificacion: ', respuesta.encoding)
respuesta.encoding = 'UTF-8'
print('como texto: ', respuesta.text)


 