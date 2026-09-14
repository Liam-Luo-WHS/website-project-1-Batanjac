#Student list

#The student names and scores will store what is entered in student_names_enter and student_scores_enter.
student_names = []
student_scores = {}
student_names_enter = ""
student_scores_enter = ""

#The code below will keep running forever.
while True:
    student_names_enter = input("Enter a name: ")
    student_names.append(student_names_enter)
    student_scores[student_names_enter] = "" #The student name entered from student_names_enter will be stored into the list.
    try:
        student_scores_enter = int(input("Enter a score: "))
        student_scores[student_names_enter] = student_scores_enter #The score associated with the student will be stored into the list.
        if student_scores_enter < 50: #If the student has a score below 50, the output will tell the user the student has failed.
            print("Student failed.")
            print(student_scores) #The student and score will be shown on the output.
        else:
            print("Student passed.")
            print(student_scores)
    except ValueError:
        print("Enter a number.")