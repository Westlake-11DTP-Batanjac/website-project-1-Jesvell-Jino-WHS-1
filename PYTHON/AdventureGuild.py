# hero system
heroes = {
    1 : {
        "name" : "Amihr the Blind",
        "level" : 0,
        "health" : 100,
        "attackPower" : 1,
        "defencePower" : 1,
        "experience" : 0,
        "class" : "Assassin"
    },
    2 : {
        "name" : "",
        "level" : 0,
        "health" : 100,
        "attackPower" : 1,
        "defencePower" : 1,
        "experience" : 0,
        "class" : ""
    },
    3 : {
        "name" : "",
        "level" : 0,
        "health" : 100,
        "attackPower" : 1,
        "defencePower" : 1,
        "experience" : 0,
        "class" : ""
    },
    4 : {
        "name" : "",
        "level" : 0,
        "health" : 100,
        "attackPower" : 1,
        "defencePower" : 1,
        "experience" : 0,
        "class" : ""
    },
    5 : {
        "name" : "",
        "level" : 0,
        "health" : 100,
        "attackPower" : 1,
        "defencePower" : 1,
        "experience" : 0,
        "class" : ""
    },
    6 : {
        "name" : "",
        "level" : 0,
        "health" : 100,
        "attackPower" : 1,
        "defencePower" : 1,
        "experience" : 0,
        "class" : ""
    }
}

# money system
startingGold = 100
shopItems = {
    "Healing Potion" : 20,
    "Iron Shortsword" : 100,
    "Stick" : 2
}

# battle system
gameloop = True

# player data
playerName = ""


# intro
print("""Welcome to an average adventure!
I am the wizard of Amihr, my name is Thomas.
I will grant you my weakest clone, Amihr the Blind.
Defeat the demon lord and conquer the lands of Astravia.""")

# getting player data
playerName = input("What is your name adventurer?")

pause = input("Ready to start " + playerName + "?")

while gameloop == True:
    print("The morning arrives...")
    ask = input("What do you want to do?(Shop/Rest/Train): ")
    ask = ask.lower().split()
    for i in ask:
        if i == "shop":
            pass
