from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask (__name__)



data = []



@app.route('/', methods=['GET'])

def index():
    global data
    data = db.getEvents()
    print(data)
    return render_template('agenda.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    number = request.form['number']
    db.insert_event(name, number)
    print("Datos enviados ", name, number)
    return redirect(url_for('index'))

def hello_world():
    return 'Hola mundo Flask prueba'

if __name__ == '__main__':
    
    app.run(debug=True)
