def get_integer():
    while True:
        try:
            number = input("Enter a whole number. ")
            print(int(number))
            break
        except ValueError as e:
            print("Error:", e)

get_integer()