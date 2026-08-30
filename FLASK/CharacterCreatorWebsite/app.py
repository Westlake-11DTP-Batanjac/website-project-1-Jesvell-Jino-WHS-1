from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/")
def aboutme():
    return render_template("index.html")

@app.route("/createcharacter", methods=["POST"])
def createcharacter():
    name = request.form.get("name")

    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)
