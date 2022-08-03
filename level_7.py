from math import sqrt # we will use this in testing if the number is prime
num = 1 # starting point 
counter = 0 # used to count what number prime it is up to
while counter < 10001: # once the counter reaches 10001 we are done
  num += 1 # we add 1 to the number up here because if we have it at the end it will add one an extra time
  condition = False # we start with this being false and assume that no matter what the number is, it is prime until we show that it isn't
  for i in range(2,int(sqrt(num)+1)): # starting at 1 is not go
    if num % i == 0: # if the number is not prime we set the condition to true so our counter doesn't increase
      condition = True
      break
  if condition == False: # if our assumption was right we can increase our counter by 1
    counter += 1
print(num) # print the 10001st prime 