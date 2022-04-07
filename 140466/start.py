from distutils.log import error
from email.mime import image
from flask import Flask, render_template, request
import random
import start
app = Flask(__name__, static_url_path='/files')
app.config['SECRET_KEY'] = 'VERY_SECRET_KEY'
table = [('log1','pas')]

def filters(filt,inp):
    test_f = 0
    for i in inp:
        if i[0] == filt:
            test_f = 1
    if test_f == 0:
        return True
    else:
        return False

@app.route('/')
def start():
    return render_template('start.html', username="1",table = table)

@app.route('/register', methods=['POST', 'GET'])
def register ():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        if filters(request.form['email'],table):
            table.append((request.form['email'],request.form['password']))
        else:
            print("error")
        return '<meta http-equiv="refresh" content="0;URL=/result" />'

@app.route('/result')
def result ():
    return render_template('sucress.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
