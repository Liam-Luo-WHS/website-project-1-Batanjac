while True:
    user_input = input("Password? ")
    if user_input == "secure123":
        print("Access granted.")
        break
    else:
        print("Access denied.")