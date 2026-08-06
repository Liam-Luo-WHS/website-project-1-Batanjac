num = int(input("Number? "))
a=num//2
counter=0
for i in range (a):
    if num%(i+1)==0:
        counter=counter+1
if counter>1:
    print(num, " is not a prime number.")
else:
    print(num, " is a prime number.")