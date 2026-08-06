import random

answer = [
    # Positive
    "It is certain",
    "Without a doubt",
    "You may rely on it",
    "Signs point to yes",
    "Outlook good",
    
    # Neutral
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    
    # Negative
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]
usedanswers = []

while True:
    while True:
        ask = input("Ask a question: ")
        try:
            ask = int(ask)
        except:
            if ask != "":
                while True:
                    ran = random.randint(0, 14)
                    if ran in usedanswers:
                        continue
                    elif len(usedanswers) == 15:
                        usedanswers = []
                    else:
                        print("Magic 8Ball:", answer[ran])
                        usedanswers.append(ran)
                        break
            else:
                print("Can you please write an actual question please?")
                continue
        else:
            continue
    ask = input("Do you want to stop?(Y/N): ")
    if ask == "Y":
        break