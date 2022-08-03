from collections import deque # we will be using a deque to truncate our number
from tools import prime_tester
def deque_to_num(x):
    return int(''.join(x))
def truncate_right(num): # in this method we want to continuously remove numbers from the right
    while True: # we want to keep trying this until we either know it satisfies the condition entirely or exit early if it doesn't
        num.pop() # removes the rightmost number
        if len(num) == 0: # we have this check early because otherwise the program will cause an error when there are no numbers left for it to check 
            return True
        if prime_tester(deque_to_num(num)): # after we remove a number from the deque we want to convert it into a string then an integer to use it as an actual number for prime_tester, the advantage to putting the conversion here is that we are only temporarily converting it just for this check, so we don't have to convert it back to a deque 
            continue # if the truncated number is prime then restart and keep going
        else:
            return False # exit if it fails once
def truncate_left(num): # same idea as truncate_right only removing from the left
    while True:
        num.popleft()
        if len(num) == 0: 
            return True
        if prime_tester(deque_to_num(num)):
            continue
        else:
            return False
nums = [] # this list of numbers will hold all of the numbers that satisfy our condition 
counter = 2 # the idea is to have this number go up and we don't actually alter it at all, we want to "capture" it in a given moment to test it
#while len(nums) < 1:
while len(nums) < 11:
    if counter == 2 or counter == 3 or counter == 5 or counter == 7:
        counter += 1
        continue # skip over these because they won't be included in the result
    if prime_tester(counter): # test if the number is prime then we will test if the truncated parts of it are 
        counter_left, counter_right = deque(str(counter)), deque(str(counter))  # convert the counter into a string and then a deque, we want two because otherwise the original counter will be altered, and it resets every time because this is where it gets reassigned 
        if truncate_left(counter_left) and truncate_right(counter_right): # if the number is still prime while truncating parts off in both directions then it qualifies for our list
            nums.append(counter)
            counter += 1
            continue  
    counter += 1 # iterate to the next number
print(sum(nums))


