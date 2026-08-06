year = input("Year? ")
if int(year) % 4 == 0:
    print("This is a leap year.")
elif int(year) % 100 == 0 and int(year) % 400 == 0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")