from flask import Flask
from flask import render_template
import requests
import json


current_directory = "NONe"
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Worldaa!'

@app.route('/consultar')
def consulta(id=None):
    params = {'company':'1', 'searchType':'nro_suministro','client':'3281167-1', 'dtmId':'account payment'}
    response = requests.post('https://www.enel.cl/es/clientes/servicios-en-linea/pago-de-cuenta.mdwedge.getSupplyDetail.html', data = params)
    factura=json.loads(response.text)['supplyBalance']
    return render_template('consulta.html', monto=factura)

@app.route('/lista/')
def hello(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()