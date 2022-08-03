total = 1 # start with 1 
for x in range(100,1,-1):
  total *= x # acts as 100!
total = list(str(total)) # convert the number into a string and make a list that has each digit as an index
for y in range(len(total)): # convert the numbers from strings to integers 
  total[y] = int(total[y])
print(sum(total)) # find the sum of the list 