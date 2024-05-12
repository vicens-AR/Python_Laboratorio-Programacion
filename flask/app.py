from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
  app.run(debug = True, port=5000)
  
@app.route('/')
def casa():
    return render_template('Home.html')

@app.route('/Contacto')
def Contact():
    return render_template('Contacto.html')

@app.route('/Curiosidades')
def Curiosidad():
    return render_template('Curiosidades.html')

@app.route('/Info_Flask')
def Info():
    return render_template('Info_Flask.html')