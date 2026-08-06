number_1 = input("First number? ")
number_2 = input("Second number? ")

if number_1 == number_2:
    print("Both numbers are equal.")
elif number_1 > number_2:
    print(number_1 + " is larger than " + number_2 + ".")
elif number_2 > number_1:
    print(number_2 + " is larger than " + number_1 + ".")