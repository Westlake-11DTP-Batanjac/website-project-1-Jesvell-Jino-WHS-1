from flask import Flask 

app = Flask(__name__) 

@app.route("/") 
def home(): 
    return "<h1>Jesvell Jino</h1>" 

@app.route("/hobbies") 
def hobbies(): 
    return "<ul><li>Gaming<li>Eating<li>Coding<ul>"

if __name__ == "__main__": 
    app.run(debug=True)