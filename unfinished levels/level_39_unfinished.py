maximized = 0
maximized_p = 0
p=0
while p <= 1000:
    nums = [] # this list will hold all of the numbers that meet the condition of making a right triangle and adding up to a perimeter, every 3 numbers are a group for it
    # see later for the use of these next two lists 
    temp = [] 
    num_of_sols = []
    # 3x nested for loop going from 1 through whatever the current value of p is
    for a in range (1,p+1):
        for b in range(1,p+1):
            for c in range(1,p+1):
                # we want to make sure that abc make a right trianlge and then see if their sum is equal to p (the perimeter of the sides)
                if (a**2 + b**2) == c ** 2 and a + b + c == p:
                    if a in nums or b in nums or c in nums: # if it is and already in the list then we don't want to re-add them, we don't use a set because the set is unordered which matters for this
                        pass
                    else: # if they're not in the list then we append the and have it so every 3 make up the solutions we want
                        nums.append(a)
                        nums.append(b)
                        nums.append(c)
    for i in nums: # we want to iterate thorugh our list of numbers, every 3 go into a list and we want to put this list into another list that will total the number of solutions we have
        temp.append(i)
        if len(temp) == 3:
            num_of_sols.append(temp)
            temp = [] # make it blank after so we only ever at most have 3 elements in here
    if len(num_of_sols) > maximized:
        maximized = len(num_of_sols) # if it was higher than the previous amount of sols 
        maximized_p = p # the value of p at this point in time 
    p += 1
    print(p)

print(maximized_p) # highest value for p
print(maximized) # no. of sols 