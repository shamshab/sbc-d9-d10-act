from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    birthdate = request.form['birthdate']
    birthdate_obj = datetime.strptime(birthdate, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate_obj.year - ((today.month, today.day) < (birthdate_obj.month, birthdate_obj.day))
    
    return f'Name: {name}<br>Age: {age}'

if __name__ == '__main__':
    app.run(debug=True)
