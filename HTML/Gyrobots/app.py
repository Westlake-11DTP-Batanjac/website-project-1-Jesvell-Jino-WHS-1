from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

database = 'messages.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(database)
        g.db.row_factory = sqlite3.Row  # Keeping your row factory configuration!
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    
    # Open and execute your SQL schema script
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

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
        "network.html",
        fname=fname,
        lname=lname
        )

# Custom 404 Error Handler
@app.errorhandler(404)
def page_not_found(error):
    # The 'error' argument captures the exception details
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)