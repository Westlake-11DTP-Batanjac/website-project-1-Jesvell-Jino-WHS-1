import json 

start = {
    "name" : "Jay",
    "age" : 16,
    "favourite_subject" : "",
    "learning_python" : True
}

with open(r"PYTHON\PythonJsonLearning\profile.json", "w") as sfile: 
    json.dump(start, sfile, indent=2)


with open(r"PYTHON\PythonJsonLearning\profile.json", "r") as rfile: 
    profile = json.load(rfile)
