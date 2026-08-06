#If a number is a prime number

def is_prime(n):
    if int(n) % 2 == 0: #This is supposed to calculate for a prime number, replace when I can
        return "This number is a prime number."
    return "This number is not a prime number."

print(is_prime(10))