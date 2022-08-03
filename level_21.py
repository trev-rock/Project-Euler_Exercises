# we want to find the values that match in a dictionary 
# first find all the divisors of a num 
from math import sqrt
def divisors_sum(x): 
    divisors = []
    for i in range(1,int(sqrt(x))+1): # a divisor cannot be higher than the sqrt of the num
        if x % i == 0:
            divisors.append(i)
            if i*i != x and i != 1: # if a number is a factor and it is not the sqrt of the original number then we want to divide the original number by that number to get its counterpart factor, saves steps of needing to iterate through every value
                divisors.append(int(x/i))
    return sum(divisors)

pairs = set()
for g in range(1,10000):
    for h in range(1,10000):
        if divisors_sum(g) == h and divisors_sum(h) == g and g != h:
            pairs.update([g,h])
print(pairs)
print(sum(pairs))