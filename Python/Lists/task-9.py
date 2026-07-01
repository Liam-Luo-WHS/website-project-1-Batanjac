#Check for prime numbers
#The terminal has to be killed every time after the code is run in order for it to work properly

number = int(input("Enter a number. "))
if number % 2 != 0:
    print("This is a prime number.")
else:
    print("This is not a prime number.")