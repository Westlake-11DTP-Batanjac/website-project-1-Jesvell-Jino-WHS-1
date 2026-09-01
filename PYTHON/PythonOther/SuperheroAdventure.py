hero_name = input("What is your hero name?: ")
while True:
    try:
        hero_age = int(input("What is your age?: "))
    except:
        print("Not a valid integer(number), try again.")
    else:
        break

powers = { 
    1: "Flying", 
    2: "Invisibility", 
    3: "Super Strength", 
    4: "Chimeration", 
    5: "Fire Force",
    6: "Time Travel"
}

weaknesses = {
    "Flying" : "Strong Wind",
    "Invisibility" : "Paint",
    "Super Strength" : "Small Things",
    "Chimeration" : "Weak Animals",
    "Fire Force" : "Water",
    "Time Travel" : "Unlucky Travels"
}

print("Choose from these powers...\n")
for number, power in powers.items():
    print(number, ":", power)

choice = int(input("What is your choice?"))
selected_power = powers[choice]