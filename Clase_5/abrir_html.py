import pprint

htlm = open('pagina_web.html', encoding = 'utf-8')
for linea in htlm:
    pprint.pprint(linea)