from flask import Flask, render_template, request
from flask import redirect, render_template,url_for
from code_check_1 import scrappy_fun


app = Flask(__name__)
app.config['SECRET_KEY'] = "isabella"

@app.route('/', methods=["POST", "GET"])     #Routing url for the app.
def index():
    if request.method=="POST":
        pdb_id= request.form["floatingTextarea"].strip().split()
        print(f"multiple id are:{pdb_id}")
        return redirect(url_for("uniport", uniport_id=pdb_id))
    else:
        return render_template('index.html')

@app.route('/uniport/<uniport_id>')
def uniport(uniport_id):
    if type(uniport_id) is not list:
        due =scrappy_fun([uniport_id])
    else:
        due =scrappy_fun(uniport_id)
    return render_template("user.html", uniport_id=due)

if __name__ == '__main__':
    app.run(debug=True)