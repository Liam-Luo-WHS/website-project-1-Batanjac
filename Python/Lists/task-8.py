#Multiplication table (not finished)

table = []
multiplier = 1
#the multiplier will increase by one every time one number is inputted.

number = int(input("Number? "))

for i in range(10):
    table.append(number)

for i in range(10):
    print(table * int(multiplier + 1))