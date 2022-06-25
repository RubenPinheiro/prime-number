from math import sqrt

def prime_checker(number):

    prime_validator = True

    if number == 1 or number == 2:
        print("It's a prime number.")
    
    for i in range (2, round(sqrt(number))):
        if number % i == 0:
            prime_validator = False
    
    if prime_validator:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
