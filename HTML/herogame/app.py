from flask import Flask, render_template, request

app = Flask(__name__)

site_name = "Character Creator"

@app.route('/')
def home():
    return render_template(
        'index.html',
        site_name=site_name
    )

if __name__ == "__main__": 

    app.run(debug=True, port=5000) 


if __name__ == "__main__": 

    app.run(debug=True, port=5000) 