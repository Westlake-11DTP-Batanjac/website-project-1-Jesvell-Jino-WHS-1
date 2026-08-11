import random
while True:
    ask = input("Rock, Paper, or Scissors?: ")
    plr = 0
    if ask.lower() == "rock":
        plr = 1
    elif ask.lower() == "paper":
        plr = 2
    elif ask.lower() == "scissor":
        plr = 3
    com = random.randint(1, 3)
    if plr == 1:
        if com == 3:
            print("Win!")
        elif com == 2:
            print("Lose!")
        elif com == 1:
            print("Draw!")
    elif plr == 2:
        if com == 3:
            print("Lose!")
        elif com == 2:
            print("Draw!")
        elif com == 1:
            print("Win!")
    elif plr == 3:
        if com == 3:
            print("Draw!")
        elif com == 2:
            print("Lose!")
        elif com == 1:
            print("Win!")
    else:
        print("Please right 'rock', 'paper', or 'scissor'")