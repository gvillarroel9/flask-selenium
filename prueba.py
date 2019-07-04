from flask import Flask, jsonify
from flask import render_template
import requests
from flask_cors import CORS

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os

CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')
options = Options()
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)


current_directory = "NONe"
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, Worldaa!'

@app.route('/api/factura/<client_id>')
def consulta(client_id=None):
    params = {'company':'1', 'searchType':'nro_suministro','client':client_id, 'dtmId':'account payment'}
    print(params)
    response = requests.post('https://www.enel.cl/es/clientes/servicios-en-linea/pago-de-cuenta.mdwedge.getSupplyDetail.html', data = params)
    return response.content

@app.route('/selenium/')
def hello(name=None):
    driver.get("http://www.python.org")
    element = driver.find_element_by_id("success-stories")
    name=element.text
    driver.close()
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)