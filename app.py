from flask import Flask, render_template, request, make_response
from flask import redirect, render_template
from code_check import scrappy_fun

app = Flask(__name__)
app.config['SECRET_KEY'] = "isabella"

@app.route('/')     #route url for the app
def index():
    return render_template('index.html')

@app.route('/uniport/<uniport_id>')
def uniport(uniport_id):
    uniport_id =scrappy_fun(["1mky"])
    return render_template("user.html", uniport_id=uniport_id)


if __name__ == '__main__':
    app.run(debug=True)