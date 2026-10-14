from flask import Flask, render_template, request
import sqlite3

# conn.row_factory = sqlite3.Row

app = Flask(__name__)

DATABASE = "gyrobots.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Create database table
def init_db():
    conn = get_db()

    conn.execute("PRAGMA foreign_keys = ON;")
    
    conn.execute('''
    CREATE TABLE IF NOT EXISTS profiles (
        profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
        uniquename TEXT NOT NULL UNIQUE,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL
    )
    ''')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        message_id INTEGER PRIMARY KEY AUTOINCREMENT,
        profile_id INTEGER,
        message TEXT NOT NULL,
        FOREIGN KEY (profile_id) REFERENCES profiles (profile_id) ON DELETE CASCADE
    )
    ''')

    conn.commit()
    conn.close()

def sqlCommandFetchAll(command):
    conn = get_db()
    return conn.execute(command).fetchall()

def sqlCommandCommit(command, parameters=()):
    conn = get_db()
    conn.execute(command, parameters)
    conn.commit() # Crucial for saving INSERT, UPDATE, or DELETE changes
    conn.close()


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
    uname = request.form["uname"]

    print("Checking if user is inside database...")
    existing_user = sqlCommandFetchAll(
        "SELECT * FROM profiles WHERE uniquename = ?", 
        (uname,)
    )

    if existing_user:
        print("User found!")
        return render_template(
                "network.html",
                fname=fname,
                lname=lname
                )
    else:
        return render_template(
            "network.html",
            error="Invalid unique name or credentials. Please try again!"
        )

@app.route("/register", methods=["POST"])
def register():


# Custom 404 Error Handler
@app.errorhandler(404)
def page_not_found(error):
    # The 'error' argument captures the exception details
    return render_template('404.html'), 404

if __name__ == "__main__":
    init_db()
    app.run(debug=True)