#Number guessing game

#This is the answer of the game.
answer = 15
number = ""
attempts = 0

while number != answer:
    number = int(input("Pick a number between 1 and 20: "))
    if number > answer:
        print("Too high, try again!")
    elif number < answer:
        print("Too low, try again!")
    attempts += 1
print("Well done, you got it in", attempts, "tries!")