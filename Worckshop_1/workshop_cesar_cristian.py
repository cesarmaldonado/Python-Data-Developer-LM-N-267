from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
import requests
import mysql.connector 


driver = webdriver.Chrome(executable_path= 'C:/Users\Pc\Desktop\Python\Cursos EANT\Python Data Developer\Clase_6\chromedriver.exe') 
url = 'https://supermercado.carrefour.com.ar/catalogsearch/result/?q=cerveza'
driver.get(url)


js_scroll_dar_posicion = '''
   fin_de_pantalla = document.body.scrollHeight
   window.scrollTo(0, fin_de_pantalla)
   return fin_de_pantalla
'''
sleep(3)
pos_actual = 0
pos_siguiente = driver.execute_script(js_scroll_dar_posicion)
sleep(3)

clikear_boton_js = """
    setTimeout(function(){
        document.querySelector('[class="ver-mas-productos btn meanbee-infinitescroll-button"]').click()
    }, 5000)
"""

while pos_actual != pos_siguiente:
    pos_siguiente = pos_actual
    pos_actual = driver.execute_script(js_scroll_dar_posicion)
    sleep(4)
    driver.execute_script(clikear_boton_js)
    sleep(4)
    
html = driver.execute_script("return document.documentElement.outerHTML")
dom = BS(html,features ='html.parser')
lista_producto = dom.find_all(class_="col s12 product-card product-card-food")
cervezas = []

for cerveza in range(len(lista_producto)):
    link = lista_producto[cerveza].div.a['href']  
   
    respuesta = requests.get(link)   
    respuesta.encoding ='utf-8'
    html = respuesta.text
    dom = BS(html, features='html.parser')
    
    descripcion = dom.find(class_= 'h1').text
   
    marca =  dom.find(class_='brand truncate').text
    marca= marca.replace(' ','')
   
    precio_publicado = dom.find(class_= 'price 207 precio-regular-productos-destacados').text
    precio_publicado = precio_publicado.replace(' ','')
    precio_publicado = precio_publicado.replace('$','')
    precio_publicado = precio_publicado.replace(',','.')
        # precio_publicado = float(precio_publicado)# revisar
    
    try:
        promocion = dom.find(class_ = 'offer multiline').text
        
    except:
        promocion = 'no tiene'
    
    precio_lt = dom.find(class_='price').text
        # precio_lt = precio_lt.replace('(','')
        # precio_lt = precio_lt.replace(')','')
    precio_lt = precio_lt.replace('$','')
    precio_lt = precio_lt.replace(',','.')
        # precio_litro = precio_lt.split('x')
        # print(precio_lt)
    
    tipo_producto = dom.find(class_= 'info').text
    # print(tipo_producto)
      
    cervezas.append([descripcion, marca, precio_publicado, promocion, precio_lt, tipo_producto])
        
conexion = mysql.connector.connect(
                host = 'cloud.eant.tech',
                database = 'pdp_base001',
                user = 'pdp_usuario001',
                password = 'eantpass')
        
cursor = conexion.cursor()

for matriz in cervezas:
    sql = "INSERT INTO cervezas (descripcion, marca, precio publicado $, promocion, precio por litro $, tipo de producto ) VALUES ('"+matriz[0]+"', '"+matriz[1]+"', '"+matriz[2]+"', '"+matriz[3]+"', '"+matriz[4]+"', '"+matriz[5]+"')"
    cursor.execute(sql)
    conexion.commit()
 
cursor.close()
conexion.close()
   
print('Los datos ya fueron cargados')        
    
        
   
