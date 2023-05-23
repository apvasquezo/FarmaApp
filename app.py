from googlemaps import client
from flask import Flask, render_template, request, redirect, url_for, jsonify
import googlemaps

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    idpersona = request.form['idpersona']
    medicamento = request.form['medicamento']
    direccion = request.form['direccion']
    # Agregar la lógica para buscar la información en una base de datos o API
    # <button type="submit" class="btn btn-primary" onclick="window.history.back()">Regresar</button>
    resultados = [
        {
            'nombre': 'Acetaminofen',
            'farmacia': 'La rebaja',
            'descripcion': 'Tabletas',
            'precio': '8000.00',
            'direccion': 'Calle 80, Medellin',
            'link': 'https://www.larebajavirtual.com/acetaminofen'
        },
        {
            'nombre': 'Dolex',
            'farmacia': 'Pasteur',
            'descripcion': 'Tableta',
            'precio': '15000.00',
            'direccion': 'Calle 94, Medellin',
            'link': 'https://www.farmaciaspasteur.com.co/dolex'
        }
    ]
    return render_template('results.html', resultados=resultados)

gmaps = googlemaps.Client(key='AIzaSyBsm0adgLvMBb1jbz2YgIDvRRSCwmoRP0M')

@app.route('/search_address', methods=['GET'])
def search_address():
    address = request.args.get('address')
    if not address:
        return jsonify({"error": "No se proporcionó una dirección"}), 400

    geocode_result = gmaps.geocode(address)

    if not geocode_result:
        return jsonify({"error": "No se encontró la dirección"}), 404

    location = geocode_result[0]['geometry']['location']

    return jsonify({"latitude": location['lat'], "longitude": location['lng']}), 200

if __name__ == '__main__':
    app.run(debug=True)