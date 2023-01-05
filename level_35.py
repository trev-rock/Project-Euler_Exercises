from collections import deque
from tools import prime_tester

def circular_check(num: int):
    num = deque(str(num)) # convert the number to a string then a deque to get each digit in its own index to rotate
    for j in range(1, len(num)): # we need to rotate as many times as the number is long, we don't need an extra + 1 at the end because we know it's original value is already prime
        num.rotate() # rotate our number by one
        copy_num = int(''.join(num)) 
        print(copy_num)
        if not prime_tester(copy_num): # convert the number back to an integer and check if it is prime, if not we stop testing
            return False
    return True


circular_nums = []

for i in range(1,1000000):
    if prime_tester(i): # test the original value first, if this isn't prime then no need to test further
        if circular_check(i): # if the number we were examining is circular, add it to our list
            circular_nums.append(i)

print(len(circular_nums))
print(circular_nums)