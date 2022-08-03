num = 2 # we start with 2 because 1 doesn't count for the sake of this problem
num_list = [] # we use this list to put in the numbers that satisfy our condition later
while num < 1000000:
  temp_list = list(str(num)) # convert the number that we are on into a string then split it up further by putting each digit into their own index in a list 
  for i in range(len(temp_list)): # iterate through this list and convert each string version of a digit into an integer and raise it to the 5th power 
    temp_list[i] = int(temp_list[i]) ** 5
  if sum(temp_list) == num: # take the sum of that list and see if it is equal to the original number we broke down, if it is then the numebr can be added to our main list 
    num_list.append(num)
  num += 1 # n to the next value 

print(sum(num_list)) # take the final sum at the end