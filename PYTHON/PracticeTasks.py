student_names = [] # list of student names
student_scores = {} # dictionary to store scores
# a space
number_of_students = int(input("How many students do you have?: ")) #find how many studdent
for students in range(number_of_students): # for each student ask their name and score
    name = input("What is the student " + str(students) + " ") # ask for the name
    while True:
        try:
            score = int(input("What is the score for that student: "))
        except:
            print("Not a valid integer, do it again.")
        else:
            break

for students in range(number_of_students):

    if score >= 50:
        print(students)
