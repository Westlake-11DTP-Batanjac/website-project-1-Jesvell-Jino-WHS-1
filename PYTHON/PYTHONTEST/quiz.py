import json 

with open(r"PYTHON\PYTHONTEST\quiz_data.json", "r") as rfile: 
    player_stats = json.load(rfile) # loads the player's score

player_stats["score"] = 0
yorn = input("Do you want to erase your highscore?: ") # ask if they want to erase their highscore
if yorn.lower() == "y":
    player_stats["highscore"] = 0

quiz = { # quiz data
    "question_amount" : 5,
    "questions" : { # question type answer multichoices
        1 : ["What year was the sitcom Friends first aired?", "number", 1994],
        2 : ["Is the tv show Friends a sitcom?", "truefalse", "true"],
        3 : ["Who is the richest Friends actor?", "multi", "Jennifer Aniston", ("Jennifer Aniston", "Courteney Cox", "David Schwimmer", "Matt LeBlanc")],
        4 : ["Which 'friend' is a clean freak?", "open", "Monica Geller"],
        5 : ["Which two 'friends' are siblings?", "open", "Monica and Ross Geller"]
    }
}


for question_number in range(1, (quiz["question_amount"] + 1)): # loop for all the questions
    question = quiz["questions"][question_number][0]
    question_type = quiz["questions"][question_number][1]
    question_answer = quiz["questions"][question_number][2]

    print(question)
    while True:
        answer = input("What is your answer?: ")
        if question_type == "number":
            try:
                if int(answer) == question_answer:
                    player_stats["score"] += 1
            except:
                print("Please write a number")
                continue
            else:
                break
        elif question_type == "truefalse":
            if answer.lower() == question_answer:
                player_stats["score"] += 1
                break
        else:
            if answer == question_answer:
                player_stats["score"] += 1
                break
        break

# save the score
with open(r"PYTHON\PYTHONTEST\quiz_data.json", "w") as sfile: 
    json.dump(player_stats, sfile, indent=2)