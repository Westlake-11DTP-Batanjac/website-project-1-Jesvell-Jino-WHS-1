import random

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
# 1 Items, 2 Weapons, 3 Armors, 4 Pets
shopItems = {
    # Consumable Items (1000)
    1001 : {
        "Name" : "Health Potion",
        "Cost" : 5,
        "Healing" : 5
    },
    1002 : {
        "Name" : "Greater Health Potion",
        "Cost" : 15,
        "Healing" : 20
    },
    1003 : {
        "Name" : "Mega Health Potion",
        "Cost" : 40,
        "Healing" : 60
    },
    1004 : {
        "Name" : "Revive Scroll",
        "Cost" : 100,
        "Healing" : 999
    },
    1005 : {
        "Name" : "Energy Drink",
        "Cost" : 10,
        "Healing" : 10
    },
    1006 : {
        "Name" : "Mystery Soup",
        "Cost" : 8,
        "Healing" : 15
    },
    1007 : {
        "Name" : "Dragon Steak",
        "Cost" : 50,
        "Healing" : 100
    },
    # Weapons (2000)
    2001 : {
        "Name" : "Iron Sword",
        "Cost" : 20,
        "Damage" : 5
    },
    2002 : {
        "Name" : "Steel Sword",
        "Cost" : 50,
        "Damage" : 10
    },
    2003 : {
        "Name" : "Knight's Claymore",
        "Cost" : 100,
        "Damage" : 18
    },
    2004 : {
        "Name" : "Shadow Dagger",
        "Cost" : 80,
        "Damage" : 14
    },
    2005 : {
        "Name" : "Thunder Hammer",
        "Cost" : 150,
        "Damage" : 25
    },
    2006 : {
        "Name" : "Dragon Slayer",
        "Cost" : 350,
        "Damage" : 50
    },
    2007 : {
        "Name" : "Celestial Blade",
        "Cost" : 600,
        "Damage" : 80
    },
    2008 : {
        "Name" : "Stick Found Outside",
        "Cost" : 1,
        "Damage" : 1
    },
    2009 : {
        "Name" : "Banana Launcher",
        "Cost" : 75,
        "Damage" : 12
    },
    2010 : {
        "Name" : "The Fish",
        "Cost" : 999,
        "Damage" : 99
    },
    # Armors (3000)
    3001 : {
        "Name" : "Iron Chestplate",
        "Cost" : 30,
        "Defence" : 10
    },
    3002 : {
        "Name" : "Steel Armor",
        "Cost" : 70,
        "Defence" : 18
    },
    3003 : {
        "Name" : "Knight Armor",
        "Cost" : 120,
        "Defence" : 28
    },
    3004 : {
        "Name" : "Dragon Scale Armor",
        "Cost" : 300,
        "Defence" : 50
    },
    3005 : {
        "Name" : "Celestial Plate",
        "Cost" : 600,
        "Defence" : 80
    },
    3006 : {
        "Name" : "Wizard Robe",
        "Cost" : 90,
        "Defence" : 15
    },
    3007 : {
        "Name" : "Cardboard Box",
        "Cost" : 2,
        "Defence" : 1
    },
    3008 : {
        "Name" : "Golden Crown",
        "Cost" : 500,
        "Defence" : 35
    },
    # Pets (4000)
    4001 : {
        "Name" : "Pretty Princess",
        "Cost" : 6,
        "Special" : "Damage",
        "Damage" : 3
    },
    4002 : {
        "Name" : "Tiny Dragon",
        "Cost" : 120,
        "Special" : "Damage",
        "Damage" : 12
    },
    4003 : {
        "Name" : "Guardian Wolf",
        "Cost" : 100,
        "Special" : "Defence",
        "Defence" : 10
    },
    4004 : {
        "Name" : "Golden Fairy",
        "Cost" : 150,
        "Special" : "Healing",
        "Healing" : 5
    },
    4005 : {
        "Name" : "Ghost Cat",
        "Cost" : 80,
        "Special" : "Damage",
        "Damage" : 8
    },
    4006 : {
        "Name" : "Rock Golem",
        "Cost" : 200,
        "Special" : "Defence",
        "Defence" : 20
    },
    4007 : {
        "Name" : "Phoenix",
        "Cost" : 500,
        "Special" : "Healing",
        "Healing" : 25
    },
    4008 : {
        "Name" : "Mimic Chest",
        "Cost" : 250,
        "Special" : "Damage",
        "Damage" : 20
    },
    4009 : {
        "Name" : "Baby Kraken",
        "Cost" : 350,
        "Special" : "Damage",
        "Damage" : 30
    },
    4010 : {
        "Name" : "Tax Collector",
        "Cost" : 1000,
        "Special" : "Money"
    }
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
playerWallet = startingGold

# functions
def shop(num):
    while True:
        itemlist = []
        for i in range(num):        
            itemlist.append(shopItems[random.randint(1, (len(shopItems) - 1))])
        randshop = random.randint(1, 3)
        if randshop == 1:
            print("~~The Hangman's Shop~~")
        elif randshop == 2:
            print("~~The Blinderman's Shop~~")
        elif randshop == 3:
            print("~~The Undertaker's Shop~~")
        for i in range(len(itemlist)):
            print("Item " + i + ": " + itemlist[i])
        boughtitem = 0
        while True:
            try:
                ask = int(input("Which of my items do you want, " + playerName + "?(Num): "))
            except:
                print("That's not a number you idiot.")
            else:
                break
            if itemlist[ask] in shopItems:
                playerWallet -= shopItems[itemlist[ask]]


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
            shop(4)
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