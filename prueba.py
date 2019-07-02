from flask import Flask, jsonify
from flask import render_template
import requests
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

@app.route('/lista/')
def hello(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)