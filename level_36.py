def decimal_to_binary(d): # convert a number from decimal to binary 
  total = [] 
  while d > 0:
    dig = d % 2 
    total.append(dig) 
    d = d // 2
  total.reverse() 
  binary_string = ''
  for i in total:
    binary_string += str(i)
  return(binary_string)

nums = [] # the numbers that are palindromes in bases 2 and 10 are added to this 

for i in range(1,1000000): # the first half checks if the base 10 version is a palindrome and the second checks if base 2 is 
  if str(i) == str(i)[::-1] and str(decimal_to_binary(i)) == str(decimal_to_binary(i))[::-1] :
      nums.append(i)

print(sum(nums)) # find the sum at the end