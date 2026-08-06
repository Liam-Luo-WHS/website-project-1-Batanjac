grade = input("Numeric grade? ")
if int(grade) > 89:
    print("A")
elif int(grade) > 79:
    print("B")
elif int(grade) > 69:
    print("C")
elif int(grade) > 59:
    print("D")
else:
    print("F")