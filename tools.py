from math import sqrt
def prime_tester(x):
    if x == 1:
        return False
    for y in range(2, int(sqrt(x)+1)): # we only need to test until the square root of the number because if it has a factor below that number then it has one above, vice versa
        if x % y == 0:
            return False
    return True