from flask import Flask, jsonify
from flask import render_template
import requests
from selenium import webdriver
from flask_cors import CORS


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
    chrome_options = Options()
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    driver.get("http://www.python.org")
    element = driver.find_element_by_id("success-stories")
    name=element.text
    driver.close()
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)