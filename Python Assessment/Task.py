#On Teams, the program does not run properly because of line 44. The f-string does not function properly on the Teams assignment. The program runs properly on Visual Studio Code.

#Dwayne Johnson quiz

#These messages appear when the user opens the quiz to tell the user what to do.
print("Welcome to the quiz about Dwayne Johnson! Can you correctly answer 5 questions?")
print() #The empty print lines are spacing between the lines to make the sentences easier to read.
print("Get at least half or more correct questions to win!")
print()

#These are important variables to make sure the quiz runs through the questions properly, and determine if the user wins or loses.
correct_answers = 0
question_number = 1

#All of the questions, answer and responses for when a user answers a question incorrectly are stored here, and can be easily modified.
questions_and_answers = {
    "all_questions": {
        1: "Dwayne Johnson voice acted Maui in the 2016 film “Moana” (True/false): ",
        2: "What video game character does Dwayne Johnson act as in the 2017 film “Jumanji: Welcome to the Jungle”?: ",
        3: "How many “Fast and Furious” related films has Dwayne Johnson acted in?: ",
        4: 'What is the only movie Dwayne Johnson acted in in 2002? "A. Be Cool", "B. The Scorpion King", "C. Southland Tales", "D. The Mummy Returns" (Answer with a letter): ',
        5: "Complete the title of the 2017 documentary featuring Dwayne Johnson: Rock and a Hard _____: "
        },
    "all_answers": {
        1: "True",
        2: "Dr. Smolder Bravestone",
        3: "6",
        4: "B",
        5: "Place"
    },
    "correction": {
        1: 'The answer is "True", Dwayne Johnson voice acted Maui!',
        2: "Wrong, Dwayne Johnson acted as Dr. Smolder Bravestone.",
        3: "Wrong, Dwayne Johnson acted in 6 “Fast and Furious” films.",
        4: 'The answer is "B", Dwayne Johnson only acted in The Scorpion King.',
        5: 'Wrong, The title is "Dwayne Johnson: Rock and a Hard Place."'
    }
    }

#The code below checks two things, if 5 questions were answered, and if the question was answered correctly or not.

while question_number != 5: #The program will show each question below until 5 are shown.

    question = input(f"{question_number}. {questions_and_answers["all_questions"][1]}") #The numbers will show the question associated with it and the number of the question.
    if question == questions_and_answers["all_answers"][1]: #The code below checks if the user's answer is correct.
        print("Correct!")
        correct_answers += 1
    else: #Answering a question wrong will tell the user they are wrong and the correct answer for the question.
        print(questions_and_answers["correction"][1]) #The program shows the answer allocated with the number in the "correction" dictionary.
    print()
    question_number += 1 #Adding 1 to the question number variable will tell the computer to check if the question number counter reached 5.
    print(correct_answers, "of", question_number, "questions answered correctly.")
    print()

    question = input(f"{question_number}. {questions_and_answers["all_questions"][2]}")
    if question == questions_and_answers["all_answers"][2]:
        print("Correct!")
        correct_answers += 1
    else:
        print(questions_and_answers["correction"][2])
    print()
    question_number += 1
    print(correct_answers, "of", question_number, "questions answered correctly.")
    print()

    question = input(f"{question_number}. {questions_and_answers["all_questions"][3]}")
    if question == questions_and_answers["all_answers"][3]:
        print("Correct!")
        correct_answers += 1
    else:
        print(questions_and_answers["correction"][3])
    print()
    question_number += 1
    print(correct_answers, "of", question_number, "questions answered correctly.")
    print()

    question = input(f"{question_number}. {questions_and_answers["all_questions"][4]}")
    if question == questions_and_answers["all_answers"][4]:
        print("Correct!")
        correct_answers += 1
    else:
        print(questions_and_answers["correction"][4])
    print()
    question_number += 1
    print(correct_answers, "of", question_number, "questions answered correctly.")
    print()

    question = input(f"{question_number}. {questions_and_answers["all_questions"][5]}")
    if question == questions_and_answers["all_answers"][5]:
        print("Correct!")
        correct_answers += 1
    else:
        print(questions_and_answers["correction"][5])
    print()
    question_number += 1
    question_number -= 1 #This line makes sure the total score out of the amount of questions is correct.
    print(correct_answers, "of", question_number, "questions answered correctly.")
    print()

    #This checks if the user got half the questions correct, and gives them the appropriate response depending on their result.
    if correct_answers >= question_number / 2:
        print("Congratulations, you win and got over or half the questions right!")
        print()
        print(correct_answers, "of", question_number, "questions answered correctly.")
    else:
        print("Sorry, you lost. You got under half the questions right.")
        print()
        print(correct_answers, "of", question_number, "questions answered correctly.")