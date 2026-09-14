#Lucky draw game

import random

people = 1
list = []

for person in range(5):
    participant = input(f"Enter participant {people}: ")
    list.append(participant)
    people += 1
print(list) #Figure out how to get a random person from a list