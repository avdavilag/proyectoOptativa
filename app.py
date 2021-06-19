from flask import Flask, render_template, url_for, jsonify, request
import decodificar, faces

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return "<p>Hello, World!</p>"
    return render_template('index.html')

@app.route('/codificar-imagen', methods=['POST'])
def codificar_imagen():
    data = request.get_json()
    text_input = data['url']
    response = decodificar.get_PhotoMessague(text_input)
    response= response["regions"][0]["lines"]
    lista = list()

    for retro in response:
        retro=retro['words']
  #print(retro[0]['text'])
        for re in retro:
            re=re['text']
            lista.append(re)
    return jsonify(lista)

@app.route('/faces',methods=['POST'])
def faces_insert():
    datos= request.get_json()
    texto_ingreso=datos['url']
    respuesta= faces.reconocimiento(texto_ingreso)
    return jsonify(respuesta)