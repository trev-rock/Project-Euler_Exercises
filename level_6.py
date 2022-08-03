sum_of_squares = [] # list that will be used to sum everything
for i in range(1,101): # because we are using the first 100 natural numbers 
  sum_of_squares.append(i**2) # square the number and add it to the list 
num_1 = sum(sum_of_squares) # take the sum of the first 100 natural numbers squared
square_of_sum = [] # same as line 1
for i in range(1,101): # same as line 2
  square_of_sum.append(i) # add the natural number to the list
num_2 = sum(square_of_sum)**2 # add all of the numbers in the list togetehr then square the result
print(num_2-num_1) # finding the difference