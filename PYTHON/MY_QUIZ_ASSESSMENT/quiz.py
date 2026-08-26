import json 

with open(r"PYTHON\PYTHONTEST\quiz_data.json", "r") as rfile: 
    player_stats = json.load(rfile) # loads the player's score

player_stats["score"] = 0
yorn = input("Do you want to erase your highscore?: ") # ask if they want to erase their highscore
if yorn.lower() == "y":
    player_stats["highscore"] = 0

quiz = {
    "question_amount": 10,
    "questions": { # question, question_type, question_answer, multi_choices
        1 : ["How many main housemates live on the cul de sac?", "number", 6],
        2 : ["Is the cul de sac located in a suburban neighbourhood?", "truefalse", "true"],
        3 : ["Who is known as the biggest troublemaker on the cul de sac?", "multi", 1, ("Edie", "Bree", "Susan", "Lynette")],
        4 : ["What is the name of the street where the characters live?", "open", "wisteria lane"],
        5 : ["How many children does Lynette have?", "number", 5],
        6 : ["Is Bree known for being extremely tidy and organised?", "truefalse", "true"],
        7 : ["Which character is a former model?", "multi", 4, ("Susan", "Bree", "Lynette", "Gabrielle")],
        8 : ["What is the name of Susan's daughter?", "open", "julie"],
        9 : ["Is Mike Delfino originally from Wisteria Lane?", "truefalse", "false"],
        10 : ["Which character is married to Carlos Solis?", "multi", 2, ("Bree", "Gabrielle",  "Susan", "Lynette")]
    }   
}

def check_answer(question_num, ans):
    question_ans = quiz["questions"][question_num][2]
    if ans == question_ans:
        return True
    else:
        return False

for question_number in range(1, (quiz["question_amount"] + 1)): # loop for all the questions
    question = quiz["questions"][question_number][0] # import the quiz question
    question_type = quiz["questions"][question_number][1] # import the quiz type
    question_answer = quiz["questions"][question_number][2] # import the quiz answer

    print(question) # ask the question
    if question_type == "multi": # check if its a multi choice question to print the multi choices
        for multichoice_choice_number in range(len(quiz["questions"][question_number][3])): # print the multi choices
            print(str(multichoice_choice_number + 1) + ": " + quiz["questions"][question_number][3][multichoice_choice_number])
    while True:
        answer = input("What is your answer?: ") # ask for the answer
        if question_type == "number": # if its a number question
            try: # try and check if it's a number
                if check_answer(question_number, int(answer)):
                    player_stats["score"] += 1
            except: # if it isnt a number ask again
                print("Please write a number")
                continue
            else: #if it's a number break
                break
        elif question_type == "truefalse": # check if its a true or false question
            if answer.lower() == "false" or answer.lower() == "true": # check if they said true or false
                if check_answer(question_number, answer.lower()): # if it's correct add to the score
                    player_stats["score"] += 1
                    break
            else:
                print("It is a true or false question. Please say true or false.") # if it isnt a true or false question say this
                continue
        elif question_type == "multi": # check if its a multi choice question
            try: # try and check if it's a number
                if int(answer) > len(quiz["questions"][question_number][3]) or int(answer) < 0:
                    raise Exception("Something went wrong!")
                if check_answer(question_number, int(answer)): # check if it's the answer
                    player_stats["score"] += 1
            except: # if it isnt a number ask again
                print("Please write a number in between 1 and", len(quiz["questions"][question_number][3]))
                continue
            else: #if it's a number break
                break
        else: # if it isnt a multi choice, true or false, or a number question do this (open question)
            if check_answer(question_number, answer.lower()): # check if its answer and then add 1 to score if it is.
                player_stats["score"] += 1
                break
        break
    print("Your score is", player_stats["score"], "out of", question_number)
        

# display score
if player_stats["score"] > player_stats["highscore"]: # check if the score is higher than the highscore
    print("New highscore!") 
    player_stats["highscore"] = player_stats["score"] # make the highscore the score
print("Your highscore:", player_stats["highscore"]) # print the highscore
# telling if they passed or not
if player_stats["score"] >= (quiz["question_amount"] // 2):
    print("You passed!")
# save the score and highscore
with open(r"PYTHON\PYTHONTEST\quiz_data.json", "w") as sfile: 
    json.dump(player_stats, sfile, indent=2)