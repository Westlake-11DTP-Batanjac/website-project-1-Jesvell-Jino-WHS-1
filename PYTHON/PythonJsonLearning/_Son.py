import json 

with open(r"PYTHON\PythonJsonLearning\profile.json", "r") as rfile: 
    profile = json.load(rfile)

name = profile["name"]
age = profile["age"]
learning_python = profile["learning_python"]


print(f"Hi, my name is {name} and i am {age} years old.")
if learning_python == False:
    print("I am not learning python!")
else:
    print("I am learning python!")