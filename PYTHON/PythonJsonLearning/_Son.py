import json 

with open("PYTHON\PythonJsonLearning\favouritefoods.json", "r") as file: 
    favourite_food = json.load(file) 

print("Your favourite food is this...") # [95, 88, 72, 100, 64]
for i in favourite_food:
    print(favourite_food)