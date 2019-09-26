from flask import Flask, jsonify
from flask import render_template
import requests
from flask_cors import CORS
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os

CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')
options = Options()
PROXY = "186.103.148.204:3128"
options.add_argument('--proxy-server=http://%s' % PROXY)
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True


current_directory = "NONe"
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api/factura/<client_id>')
def consulta(client_id=None):
    params = {'company':'1', 'searchType':'nro_suministro','client':client_id, 'dtmId':'account payment'}
    print(params)
    response = requests.post('https://www.enel.cl/es/clientes/servicios-en-linea/pago-de-cuenta.mdwedge.getSupplyDetail.html', data = params)
    return response.content

@app.route('/api/factura/aguasandinas/<client_id>')
def hello(client_id=None):
    #driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
    driver.get("https://www.aguasandinas.cl/web/aguasandinas/pagar-mi-cuenta")
    actual =str(client_id[:client_id.find("-")])
    elem = driver.find_element_by_id("busqueda_n_cuenta")
    time.sleep(1)
    elem.click()
    elem = driver.find_element_by_id("buscador_cuenta")
    elem.send_keys(actual)
    content = driver.find_element_by_css_selector('#buscar_cuenta input.boton')
    time.sleep(1)
    content.click()
    elem = driver.find_element_by_id("radio1")
    time.sleep(1)
    elem.click()
    content2 = driver.find_element_by_css_selector('.md-izq input')
    time.sleep(1)
    content2.click()
    content3 = driver.find_elements_by_css_selector('.box_celda label')
    name=content3[3].text
    driver.close()
    return jsonify({'factura': name})

@app.route('/api/cat/<client_id>')
def cat(client_id=None):
    
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
    driver.get("https://parts.cat.com/en/finningchile/"+client_id)
    name = driver.find_elements_by_css_selector('.main_header')
    time.sleep(2)
    price = driver.find_elements_by_css_selector('.pdp_price_new')
    time.sleep(2)
    return jsonify({'nombre': name[1].text, 'price': price[0].text, 'priceAux': price[1].text})

@app.route('/apiv2/cat/<client_id>')
def catv2(client_id=None):
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
    driver.get("https://parts.cat.com/en/finningchile/"+client_id)
    driver.get("https://parts.cat.com/CATFetchDealerPriceControllerCmd?globalItems="+client_id+"-PRODUCT&storeId=20261&langId=-24&catalogId=10051&outputData=0&fromPage=pdpPage&scQty=1")
    elem = driver.find_elements_by_tag_name("pre")
    time.sleep(1)
    return elem[0].text



if __name__ == '__main__':
    app.run(debug=True)