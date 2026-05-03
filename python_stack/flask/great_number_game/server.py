from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    if 'guess' in request.form and request.form['guess']:
        guess_val = int(request.form['guess'])
        if guess_val < session['number']:
            session['result'] = 'too_low'
        elif guess_val > session['number']:
            session['result'] = 'too_high'
        else:
            session['result'] = 'correct'
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)