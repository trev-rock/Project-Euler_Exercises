def examine(x):
    factors = [] # holds the factors of x
    for i in range(1,x): # finds the factors of x 
        if x % i == 0:
            factors.append(i)
    total = sum(factors) # take their sum
    if total == x:
        return "perfect"
    elif total < x:
        return "deficient"
    elif total > x:
        return "abundant"
list_of_all_nums = list(range(1,28124))
nums = {}
for i in list_of_all_nums:
    nums[i] = examine(i)
for key1, value1 in nums.items(): # find an abundant number and this will be one we will use for a bit to exhaust all of the possible sols from adding this with all other abundant nums
    if value1 == "abundant":
        for key2, value2 in nums.items(): # this generates the second abundant num to add to the first one
            if value2 == "abundant":
                sum = key1 + key2 # take their sum
                if sum > 28123: # if the sum is too large move onto the next value for value1
                    break
                if sum in list_of_all_nums: # if their sum is in the list, remove it from the result set, we want to use move instead of pop because index numbers will change as we remove elements
                    list_of_all_nums.remove(sum)
total = 0
for i in list_of_all_nums:
    total += i
print(total)