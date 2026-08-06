age = input("Age? ")

if int(age) < 13:
    print("Hi")
elif int(age) >= 13 and int(age) < 18:
    print("Hello!")
elif int(age) >= 18 and int(age) < 65:
    print("Hey!")
elif int(age) >= 65:
    print("Greetings.")