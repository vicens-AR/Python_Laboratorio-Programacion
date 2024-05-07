from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
  app.run()
  
@app.route('/')
def casa():
    return render_template('Home.html')