student_names = ["Alice", "Ben", "Charlie", "Diana", "Ethan"] # list of student names
student_scores = {} # dictionary to store scores
# a space

for names in student_names: # loop for the student names
    while True: #loop until it's correctly said right score integer
        try:
            score = int(input("What is the score for " + names + "?: ")) # ask for score
        except:
            print("Not a valid score, try again.") # if error loop again
        else:
            break #no error, break loop
    student_scores[names] = score # add to dictionary

for student in student_names: # loop for student names
    if student_scores[student] >= 50: # if the student's score is over or is 50 pass 
        print(student, "passed!")
    else:
        print(student, "failed!") #if not over or equal 50 fail them