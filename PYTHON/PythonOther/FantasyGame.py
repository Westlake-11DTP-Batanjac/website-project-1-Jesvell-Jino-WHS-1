Player = {
    "name" : "",
    "level" : 0,
    "con" : 0,
    "str" : 0,
    "int" : 0,
    "dex" : 0,
    "chr" : 0,
    "inventory" : [],
    "pets" : []
}

print("--- Welcome to Astravia ---")
print("A land where legends are forged through blood and steel.")
print("1. Train to become the strongest warrior alive.")
print("2. Hunt fearsome beasts lurking beyond the city walls.")
print("3. Accept dangerous guild quests for gold and glory.")

Player["name"] = input("First, i'm going to need your name: ")

print("Hi", Player["name"], "I'm the lost king of Astravia. And I have chosen you to take over my job.")
print("Now you get to choose where you want to put your stat points do it like I say.")
print("The stats you can choose and Constitution, Strength, Intelligence, Dexterity, and Charisma.")
print("You can choose from a set array or custom amount of points. Either 8 12 14 16 or do any that adds to 40 in total")

while True:
    ask = list(map(int, input("Write your states here like this [CON STR INT DEX CHR](set; 8 12 12 14 16): ")))
    if sum(ask) > 52 and sum(ask) < 52:
        print("You little baka. I told you it has to sum 40.")
    else:
        break