word = input("Word? ")
letter = input("Letter? ")

if letter in word:
    print(letter + " is in " + word.lower())
else:
    print(letter + " isn't in " + word.lower())