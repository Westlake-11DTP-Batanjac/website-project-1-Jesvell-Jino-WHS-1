from flask import Flask, render_template, request
import sqlite3

# conn.row_factory = sqlite3.Row

app = Flask(__name__)

DATABASE = "messages.db"

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
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        ''')
        conn.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            message_id INTEGER PRIMARY KEY AUTOINCREMENT,
            profile_id INTEGER,
            message TEXT NOT NULL,  -- 3. FIXED: Added the missing comma here!
            FOREIGN KEY (profile_id) REFERENCES profiles (profile_id) ON DELETE CASCADE
        )
        ''')

    conn.commit()
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
    init_db()
    app.run(debug=True)