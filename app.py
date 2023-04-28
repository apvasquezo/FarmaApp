from flask import Flask, render_template

app=Flask(__name__) #instancia que siempre se usa

@app.route("/")# decorador (ruta o url)
def index():#la funcion es la vista
    medica=['Dolex', 'Acetaminofen', 'Advil', 'Buscapina']
    data={#diccionario
        'titulo':'FarmaApp',
        'bienvenida':'Todo a un Click',
        'medica':medica,
        'numero_medica':len(medica)
    }
    return render_template('index.html', data=data)

if __name__=='__main__':
    app.run(debug=True, port=5000)


