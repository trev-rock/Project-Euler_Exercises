from math import sqrt # need for testing prime number
prime = 2 # lowest prime number so it is our starting point

def prime_tester(x):
    for y in range(2, int(sqrt(x)+1)): # we only need to test until the square root of the number because if it has a factor below that number then it has one above, vice versa
        if x % y == 0:
            return False
    return True


for x in range(3, 2000000, 2): # we start at 3 because we already are including 2 in this from line 2 where we define the variable 'prime'
    if prime_tester(x) == True: # add to our amount of primes if the x is prime
        prime += x
print(prime) # print the final result