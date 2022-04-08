from flask import Flask, render_template, request, session
import random
app = Flask(__name__, static_url_path='/files')
app.config['SECRET_KEY'] = 'VERY_SECRET_KEY'
table = []

def filters(filt,bd):
    for i in bd:
        if i[0] == filt:
            return False
    return True

def logins(log,bd):
    for i in bd:
        if i == log:
            return True
    return False
            

@app.route('/')
def start():
    print(session.get('user'))
    if session.get('user') != None:
        return render_template('start.html', user=True, user_name = 'привет, '+session.get('user'),table = table)
    else:
        return render_template('start.html',user=False ,table = table)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return '<meta http-equiv="refresh" content="0;URL=/" />'

@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if logins((request.form['email'],request.form['password']),table):
            session['user'] = request.form['email']
            return '<meta http-equiv="refresh" content="0;URL=/" />'
        return '<meta http-equiv="refresh" content="0;URL=/error" />'

@app.route('/register', methods=['POST', 'GET'])
def register ():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        if filters(request.form['email'],table) and request.form['email'] != '' and request.form['password'] == request.form['password-repeat']:
            table.append((request.form['email'],request.form['password']))
            return '<meta http-equiv="refresh" content="0;URL=/result" />'
        return '<meta http-equiv="refresh" content="0;URL=/error" />'

@app.route('/result')
def result ():
    return render_template('sucress.html')

@app.route('/error')
def error ():
    return render_template('error.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)