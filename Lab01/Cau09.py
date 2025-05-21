def is_prime_number(n):
    if(n < 1): return False;
    for i in range(2, int((n**0.5)) + 1):
        if(n%i == 0):
            return False
    return True
    
number = int(input("Enter a number: "))
if(is_prime_number(number)):
    print(number, 'is a prime number') 
else:
    print(number, "is not a prime number")  