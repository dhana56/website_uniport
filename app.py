from flask import Flask, render_template, request, make_response
from flask import redirect, render_template,url_for
from code_check import scrappy_fun

app = Flask(__name__)
app.config['SECRET_KEY'] = "isabella"

@app.route('/', methods=["POST", "GET"])     #route url for the app
def index():
    if request.method=="POST":
        pdb_id= request.form["nam"]
        print(pdb_id)
        return redirect(url_for("uniport", uniport_id=pdb_id))
    else:
        return render_template('index.html')


@app.route('/uniport/<uniport_id>')
def uniport(uniport_id):
    due =scrappy_fun([uniport_id])
    return render_template("user.html", uniport_id=due)




if __name__ == '__main__':
    app.run(debug=True)