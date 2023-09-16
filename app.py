from flask import Flask, render_template, request
from flask import redirect, render_template,url_for
# from main_1 import uni_id
from fun import scrappy_fun, uni_id, pool_process

app = Flask(__name__)

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
        due =uni_id([uniport_id])
    else:
        due =uni_id(uniport_id)
    out_put = pool_process(scrappy_fun,due)
    return render_template("user.html", uniport_id=out_put)

if __name__ == '__main__':
    app.run(debug=True)
