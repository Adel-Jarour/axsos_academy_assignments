from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/champion')
def champion():
    return "Champion!"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return (word + " ") * num

@app.errorhandler(404)
def not_found(e):
    return "Sorry, this page does not exist!", 404

if __name__ == '__main__':
    app.run(debug=True)