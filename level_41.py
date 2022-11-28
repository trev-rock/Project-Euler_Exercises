from itertools import permutations
from tools import prime_tester
nums = list(range(0,11))

def tuple_to_number(x):
    num_combo = ''.join(str(i) for i in x)
    return int(num_combo)

highest_prime = 2

for n in range(1,10): # this is where we get that we are going from 1 to n
    nums = list(range(1,n+1)) # generate the actual list of 1 to n
    permutations_list = list(permutations(nums)) # make the list of permutations
    for combo in permutations_list: # look at each combination
        num_to_check = tuple_to_number(combo) # convert each tuple into a number
        if prime_tester(num_to_check): # test the new number if it is prime
            if num_to_check > highest_prime: # if it is prime then see if it's higher than our previous highest prime
                highest_prime = num_to_check
            
print(highest_prime)