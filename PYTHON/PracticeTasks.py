student_names = ["Alice", "Ben", "Charlie", "Diana", "Ethan"] # list of student names
student_scores = {} # dictionary to store scores
# a space

for names in range(len(student_names)):
    score = int(input("What is the score for " + names + "?: "))

for names in range(student_names):
    if score >= 50:
        print(names)