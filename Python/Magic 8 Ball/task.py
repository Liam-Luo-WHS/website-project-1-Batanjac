import random
possible_answers = [
"Maybe", 
"Absolutely", 
"Absolutely not.", 
"Kinda.", 
"Not really.", 
"Could you say that again?", 
"Yes.", 
"No.", 
"Okay.", 
"Ask me later.",
"Can you not?",
"I can't answer that.",
"You can find that answer.",
"Is this a joke?",
"See you later."]
#This is the possible answers list.

answer = []
#This will be the answer shown in the output.

#def random #Use this later when I can find it.

while True: #This will run as long as the game is running.
    question = input("Ask me anything. ")
    if question == "":
        print("You didn't ask anything.")
    else:
        possible_answers = random.randrange(1, 16)
        answer.append(possible_answers)
        print(answer)

#Add an input that removes the answers variable
# Create a random number generator from 1 to 15, and the answer associated with the number gets transferred to the answer list.
# The answer gets removed from the list when the game is played again.