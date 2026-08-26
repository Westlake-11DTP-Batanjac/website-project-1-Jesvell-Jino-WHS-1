from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("GYROBOTS.html")

@app.route("/GYROBOTS.html")
def home2():
    return render_template("GYROBOTS.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/cvdl.html")
def cvdl():
    return render_template("cvdl.html")

@app.route("/mork.html")
def mork():
    return render_template("mork.html")

@app.route("/signin", methods=["POST"])
def signin():
    fname = request.form["fname"]
    lname = request.form["lname"]

    print("First name:", fname)
    print("Last name:", lname)

    return render_template("base.html", fname=fname, lname=lname)

if __name__ == "__main__":
    app.run(debug=True)