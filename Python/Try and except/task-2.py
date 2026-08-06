list = [29, 13, 65, 36, 10, 54]

try:
    index = int(input("Enter an index from 0 to 5. "))

    try:
        print(list[index])

    except IndexError as indexerror:
        print("Error: ", indexerror)

except ValueError as valueerror:
    print("Error: ", valueerror)