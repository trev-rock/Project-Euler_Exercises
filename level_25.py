a = 0 # first term of fib sequence
b = 1 # second term of fib sequence 
char = []
counter = 1
while len(char) != 1000:
  temp_a = a 
  a = b 
  b = temp_a + b # b is the current last term in the sequence 
  char = list(str(b)) # make a list of a string of b
  counter += 1 # this counts our index of what number term we are on 
print(counter)