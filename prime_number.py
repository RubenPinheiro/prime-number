#Write your code below this line 👇
from math import sqrt

def prime_checker(number):

    prime_validator = 0

    if number == 1 or number == 2:
        print("It's a prime number.")
    
    for i in range (2, round(sqrt(number))):
        if number % i == 0:
            prime_validator += 1
    
    if prime_validator == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
