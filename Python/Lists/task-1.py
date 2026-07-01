#Even or odd list

numbers = []

for i in range(5):
    num = int(input("Number? "))
    if num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
    numbers.append(num)