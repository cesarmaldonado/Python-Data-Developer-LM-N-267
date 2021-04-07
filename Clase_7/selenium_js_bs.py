from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.olx.com.ar/items/q-ASPIRADORA-PARA-AUTOS')

js_click_boton = '''
    boton = document.querySelector('[data-aut-id="btnLoadMore"]')
    boton.click()

'''
js_preguntar_boton = '''
    boton = document.querySelector('[data-aut-id="btnLoadMore"]')
    if (boton){
            return "Existe"
        } else{
            return "No existe"
        }
'''
existe_boton = driver.execute_script(js_preguntar_boton)

while existe_boton == 'Existe':
    driver.execute_script(js_click_boton)
    sleep(5)
    existe_boton = driver.execute_script(js_preguntar_boton)
                