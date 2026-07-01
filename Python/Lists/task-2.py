#Sum of positives

numbers = []

for i in range(7):
    num = int(input("Number? "))
    if num > 0:
        numbers.append(num)

print(sum(numbers)) 