from flask import Flask, render_template, request, make_response
from flask import redirect, render_template
from code_check import scrappy_fun

app = Flask(__name__)
app.config['SECRET_KEY'] = "isabella"

@app.route('/')     #route url for the app
def index():
    return render_template('index.html')

@app.route('/user/<nam>')
def user(nam):
    return render_template("user.html", user_name =nam)

if __name__ == '__main__':
    app.run(debug=True)