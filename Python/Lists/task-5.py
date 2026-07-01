#Remove negatives

list = []
positive_list = []

for i in range(6):
    number = int(input("Enter a number. "))
    list.append(number)
for j in range(6):    
    if list[j] >= 0:
        positive_list.append(list[j])

print(positive_list)