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
playerMonsterData = {
    "Slime" : {
        "Difficulty" : 0,
        "Kills" : 0,
    }, 
    "Phase Slime" : {
            "Difficulty" : 2,
            "Kills" : 0,
        }, 
    "Rock Slime" : {
            "Difficulty" : 1,
            "Kills" : 0,
        },
    "Goblin" : {
            "Difficulty" : 0,
            "Kills" : 0,
        }, 
    "Heightened Goblin" : {
                "Difficulty" : 1,
                "Kills" : 0,
            },
    "Rock Goblin" : {
                "Difficulty" : 2,
                "Kills" : 0,
            }, 
}

# functions
def shop():
    pass

# intro
print("""

~~Legends of Astravia!~~


Welcome to an average adventure!
I am the wizard of Amihr, my name is Thomas.
I will grant you my weakest clone, Amihr the Blind.
Defeat the demon lord and conquer the lands of Astravia.""")

# getting player data
playerName = input("What is your name adventurer? ")
pause = input("Ready to start " + playerName + "? ")

while gameloop == True:
    # Morning
    print("The morning arrives...")
    while True:
        ask = input("What do you want to do?(Shop/Rest/Train/info): ")
        ask = ask.lower()
        if ask == "shop":
            pass
            break
        elif ask == "rest":
            pass
            break
        elif ask == "train":
            pass
            break
        elif ask == "info":
            print("""The Shop: Go to the shop to buy items with gold or craft with other items.
Rest: Rest to heal your party members.
Train: Train your party members for them to get stronger faster.""")

    # Afternoon
    print("The afternoon arrives...")
    while True:
        ask = input("What do you want to do?(Venture/Tavern/info)")
        ask = ask.lower()
        if ask == "venture":
            pass
            break
        elif ask == "tavern":
            pass
            break
        elif ask == "info":
            print("""The Tavern: The tavern is a place to socialise and recieve quests.
Venture: Venture into unknown areas to fight battles.""")

    # Evening
    print("The evening arrives...")
    while True:
        ask = input("What do you want to do?(Sleep/Tavern)")
        ask = ask.lower()
        if ask == "sleep":
            pass
            break
        if ask == "tavern":
            pass
            break
        if ask == "info":
            print("""Sleep: Sleep to pass the night and heal some health back for your heroes.
Tavern: Socialise and recieve quests from the tavern.""")