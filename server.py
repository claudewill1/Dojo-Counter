from flask import Flask, render_template, request, redirect, session
from env.env import KEY
app = Flask(__name__)
app.secret_key = KEY
app.count = 0
@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html')

@app.route('/reset',methods=['POST'])
def reset():
    session['count'] = -1
    return redirect('/')

@app.route('/add_two',methods=['POST'])
def add_two():
    if 'count' in session:
        session['count'] += 1
    return redirect('/')

@app.route('/destroy',methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)