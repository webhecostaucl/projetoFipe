from flask import Flask, render_template, request
import json
import http.client

app = Flask(__name__)


@app.route("/value", methods=['POST'])
def values():
    codMarca = request.form.get("codMarca")
    codModelo = request.form.get("codModelo")
    year = request.form.get("year")
    tipo = request.form.get("tipo")

    conn = http.client.HTTPSConnection("parallelum.com.br")
    payload = ''
    headers = {
        'Authorization': 'Basic Og=='
    }
    conn.request("GET","/fipe/api/v1/" + str(tipo) + "/marcas/" + str(codMarca) + "/modelos/" + str(codModelo) + "/anos/"+str(year), payload, headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode('utf-8'))

    return render_template("values.html",response=data)


@app.route("/year", methods=['POST'])
def years():

    codModelo = request.form.get("model")
    codMarca= request.form.get("codMarca")
    tipo = request.form.get("tipo")

    conn = http.client.HTTPSConnection("parallelum.com.br")
    payload = ''
    headers = {
        'Authorization': 'Basic Og=='
    }
    conn.request("GET", "/fipe/api/v1/"+str(tipo)+"/marcas/"+str(codMarca)+"/modelos/"+str(codModelo)+"/anos", payload, headers)

    response = conn.getresponse()
    data = json.loads(response.read().decode('utf-8'))
    return render_template("years.html",response=data,codModelo=codModelo,codMarca=codMarca,tipo=tipo)



@app.route("/model", methods=['POST'])
def models():
    codMarca = request.form.get("manufact")
    tipo = request.form.get("tipo")
    conn = http.client.HTTPSConnection("parallelum.com.br")
    payload = ''
    headers = {
        'Authorization': 'Basic Og=='
    }
    conn.request("GET", "/fipe/api/v1/"+str(tipo)+"/marcas/"+str(codMarca)+"/modelos", payload, headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode('utf-8'))
    return render_template("models.html", response=data,codMarca=codMarca,tipo=tipo)


@app.route("/manufact", methods=['POST'])
def manufact():
    tipo = request.form.get("type")
    conn = http.client.HTTPSConnection("parallelum.com.br")
    payload = ''
    headers = {
        'Authorization': 'Basic Og=='
    }
    conn.request("GET", "/fipe/api/v1/"+str(tipo)+"/marcas", payload, headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode('utf-8'))
    return render_template("manufact.html", response=data,tipo=tipo)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html');


if __name__ == '__main__':
    app.run()
