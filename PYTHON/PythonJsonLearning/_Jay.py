import json 

favourite_foods = list(map(str, input("What are your favourite foods?: ").split()))

with open(r"PYTHON\PythonJsonLearning\favouritefoods.json", "w") as file: 
    json.dump(favourite_foods, file, indent=2) 