num_1 = input("First number? ")
num_2 = input("Second number? ")
num_3 = input("Third number? ")

if int(num_1) > int(num_2) and int(num_1) > int(num_3):
    print(num_1)
elif int(num_2) > int(num_1) and int(num_2) > int(num_3):
    print(num_2)
elif int(num_3) > int(num_1) and int(num_3) > int(num_2):
    print(num_3)