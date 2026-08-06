num = input("Number? ")
if int(num) % 3 == 0 and int(num) % 5 == 0:
    print(num + " is divisible by 3 and 5.")
else:
    print(num + " is not divisible by 3 and 5.")