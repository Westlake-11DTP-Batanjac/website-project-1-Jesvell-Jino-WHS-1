from flask import Flask, render_template

print(__name__)
app = Flask(__name__)
site_name = "Track Finder"
tracks = [ 

    {"name": "Mount Eden Loop", "length": 2.0, "grade": "Easy"}, 

    {"name": "Coast to Coast Walkway", "length": 16.0, "grade": "Medium"}, 

    {"name": "Karekare Falls", "length": 3.5, "grade": "Easy"}, 

    {"name": "Hillary Trail", "length": 70.0, "grade": "Hard"} 

]
count = len(tracks)
if count == 0:
    message = "There are NO tracks!"
elif count == 1:
    message = "There's only a SINGULAR track!!!! T_T T_T"
else:
    message = "Yayyy there is 2 or more tracks!!! :>"


@app.route("/") 
def home(): 
    return render_template("home.html", site_name=site_name, count=count, message=message)

@app.route("/tracks") 
def tracks_page(): 
    return render_template("tracks.html", site_name=site_name, tracks=tracks)

@app.route("/cars")
def cars():
    return ""

@app.errorhandler(404) 
def page_not_found(e): 
    return render_template("404.html"), 404

if __name__ == "__main__": 

    app.run(debug=True, port=5000) 