from selenium import webdriver
from time import sleep

# para que no se abra Chrome
op = webdriver.ChromeOptions()
op.add_argument('headless')

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.cuspide.com/resultados.aspx?c=Biolog%c3%ada%2c+Ciencias+de+la+Tierra(T%c3%a9cnicos)&tema=2173&por=Tema&orden=fecha', option = op)

# crea la acción de clickear
js_click_boton = '''
    botom = document.querySelector('[title="Siguiente"]')
    if (boton){
            boton.click()
    }else{
        return "Fin Página"        
        }
'''

from bs4 import BeautifulSoup

while driver.execute_script(js_click_boton) != "Fin Página":
    
    sleep(5)
    html = drive.execute_script("return document.documentElement.outerHTML")
    
    
    dom = BeautifulSoup(html, feautures = 'html.parser')
    
    articulos = dom.find_all(class_ =  )