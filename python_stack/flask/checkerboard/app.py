from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def index(x = 4, y = 8, color1 = 'red', color2 = 'black'):
    return render_template('index.html', rows=x, cols=y, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)
