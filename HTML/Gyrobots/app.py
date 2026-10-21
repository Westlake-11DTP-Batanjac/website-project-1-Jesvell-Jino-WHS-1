from flask import Flask, render_template, request
import sqlite3, time

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
        username TEXT NOT NULL,
        message TEXT NOT NULL,
        time TEXT NOT NULL,
        FOREIGN KEY (profile_id) REFERENCES profiles (profile_id) ON DELETE CASCADE
    )
    ''')

    conn.commit()
    conn.close()

def sqlCommandFetchAll(command, parameters=()):
    conn = get_db()
    if parameters:
        fetched = conn.execute(command, parameters).fetchall()
    else:
        fetched = conn.execute(command).fetchall()
    conn.close()
    return fetched

def sqlCommandFetchOne(command, parameters=()):
    conn = get_db()
    if parameters:
        fetched = conn.execute(command, parameters).fetchone()
    else:
        fetched = conn.execute(command).fetchone()
    conn.close()
    return fetched

def sqlCommandCommit(command, parameters=()):
    conn = get_db()
    if parameters:
        conn.execute(command, parameters)
    else:
        conn.execute(command)
    conn.commit() # Crucial for saving INSERT, UPDATE, or DELETE changes
    conn.close()


@app.route("/")
def index():
    return render_template("GYROBOTS.html")

@app.route("/about")
def about():
    return render_template("about.html", error="")


@app.route("/cvdl")
def cvdl():
    return render_template("cvdl.html")


@app.route("/mork")
def mork():
    return render_template("mork.html")

@app.route("/signin", methods=["POST"])
def signin():
    messages = sqlCommandFetchAll("SELECT profile_id, message, time FROM messages", ())
    fname = request.form["fname"]
    lname = request.form["lname"]
    uname = request.form["uname"]

    #sqlCommandCommit("INSERT INTO profiles (uniquename, firstname, lastname)"
    #    "VALUES (?, ?, ?)", (fname, lname, uname))

    if request.form.get("register"):
        try:
            sqlCommandCommit(
                "INSERT INTO profiles (uniquename, firstname, lastname) VALUES (?, ?, ?)",
                (uname, fname, lname)
            )
            return render_template(
                "about.html",
                error="Successfully Registered! Try logging in with the same credentials"
            )
        except sqlite3.IntegrityError:
            return render_template(
                "about.html",
                error="That unique name is already taken. Please choose another."
            )
    # Otherwise it's the sign-in button
    existing_user = sqlCommandFetchAll(
        "SELECT * FROM profiles WHERE uniquename = ?",
        (uname,)
    )
    if existing_user:
        return render_template(
            "network.html",
            fname=fname,
            lname=lname,
            uname=uname,
            messages=messages
        )
    else:
        return render_template(
            "about.html",
            error="Invalid unique name or credentials. Please try again!" 
        )

@app.route("/message", methods=["GET", "POST"])
def message():
    print(request.form)  # shows all keys and values sent
    posted_time = time.strftime("%Y-%m-%d %H:%M")
    message = request.form.get("message")
    uname = request.form.get("uname")
    lname = request.form.get("lname")
    fname = request.form.get("fname")
    display_name = f"{fname} {lname}".strip()

    row = sqlCommandFetchOne("SELECT profile_id FROM profiles WHERE uniquename=?", (uname,))
    profile_id = row["profile_id"] if row else None
    
    sqlCommandCommit(
    "INSERT INTO messages (profile_id, username, message, time) VALUES (?, ?, ?, ?)",
    (profile_id, display_name, message, posted_time)
    )

    if row is None:
        return "User not found", 404

    messages = [dict(row) for row in sqlCommandFetchAll("SELECT profile_id, username, message, time FROM messages", ())]
    print(messages)
    return render_template(
        "Network.html",
        uname=uname,
        lname=lname,
        fname=fname,
        messages=messages
    )


# time.strftime("%Y-%m-%d %H:%M")


# Custom 404 Error Handler
@app.errorhandler(404)
def page_not_found(error):
    # The 'error' argument captures the exception details
    return render_template('404.html'), 404

if __name__ == "__main__":
    init_db()
    app.run(debug=True)