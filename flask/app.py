from flask import Flask, render_template

app = Flask(__name__)
 
@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/Contacto')
def contacto():
    return render_template('Contacto.html')

@app.route('/Curiosidades')
def Curiosidades():
    return render_template('Curiosidades.html')

@app.route('/Info_Flask')
def Informacion():
    return render_template('Info_Flask.html')

if __name__ == '__main__':
    app.run(debug = True, port=5000)