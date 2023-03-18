n = int(input("Check this number: "))

def prime_checker(number=n):
    for iterator in range(2,number):
        if number % iterator == 0:
            return "Not Prime"
        else: 
            return "Prime"

print(prime_checker())
