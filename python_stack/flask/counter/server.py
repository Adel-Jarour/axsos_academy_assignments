from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'ThisIsASecretKey'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    
    if not session.get('skip_refresh_increment'):
        session['counter'] += 1
        session['skip_refresh_increment'] = False

    return render_template("index.html", counter=session['counter'])

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect(url_for('index'))

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/add_two')
def add_two():
    session['counter'] = session.get('counter', 0) + 2
    session['skip_refresh_increment'] = True
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)
