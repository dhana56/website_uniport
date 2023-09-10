from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')     #route url for the app
def index():
    return '<h1> Hello, World!</h1>'

@app.route('/user/<name>')
def user(name):
    return f" <h1> Hello, {name} </h1>"

if __name__ == '__main__':
    app.run(debug=True)