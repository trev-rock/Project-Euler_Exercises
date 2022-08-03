# https://projecteuler.net/problem=27
from math import sqrt


def prime_checker(x):  # this is to check if the number produced by the formula is prime
    # we only need to check up until the sqrt of the number, for every term under the square root there is one above it
    if x == 1:
        return False
    if x >= 0:  # if x is 0 or positive we can use this check because it will save steps in our program
        for y in range(2, int(sqrt(x) + 1)):
            if x % y == 0:
                return False
    # if x is negative we have to do this check because we can't use sqrt(x) of a negative number
    elif x < 0:
        for y in range(2, x + 1):
            if x % y == 0:
                return False

    return True


def formula(n, a, b):
    num = (n**2) + (a * n) + b
    return num


num_of_primes = 0
max_prime = 0
n = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):

        while True:
            # plugs n, a, and b into our formula to produce a number
            num = formula(n, a, b)
            # we want to know if this number is prime, if it is not then we try again from our next value b and if we reached the highest number for b then we also go to the next value for a
            if prime_checker(num) == False:
                break
            else:
                # print(f"a={a}, b={b}, n={n}"), this was a checker to make sure our values are working correctly
                # if num is prime then we increase our counter, this counter represents consecutive primes
                num_of_primes += 1
                n += 1

        if num_of_primes > max_prime:  # max_prime is the max number of consecutive primes, if the current counter is greater than it, then it becomes that number, and we save our coefficients of a and b
            max_prime = num_of_primes
            max_a = a
            max_b = b

        num_of_primes = 0  # reset our number of primes counter back to 0
        n = 0  # we need to start n back at 0 every time we reset our counter because we will have new values for either b and/or a

print(f"a = {max_a}, b = {max_b}, max consecutive number of primes = {max_prime}")
