from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("GYROBOTS.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/cvdl")
def cvdl():
    return render_template("cvdl.html")


@app.route("/mork")
def mork():
    return render_template("mork.html")

@app.route("/signin", methods=["POST"])
def signin():
    fname = request.form["fname"]
    lname = request.form["lname"]

    print("First name:", fname)
    print("Last name:", lname)

    return render_template(
        "base.html",
        fname=fname,
        lname=lname
    )

if __name__ == "__main__":
    app.run(debug=True)