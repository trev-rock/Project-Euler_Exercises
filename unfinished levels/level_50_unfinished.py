def prime_factorization(n): #we need to make a function that does what we need 
  prime_factors =[] #create an empty list for all of the prime factors to go into later
  p = 2 #same reasoning as before as to why we start with 2
  while n != 0:
    if n >= p: #n has to be greater than or equal to p because we have to divide by it later 
      if n % p == 0: #check to see if p is a factor of n
        prime_factors.append(p) #if it is a factor of n then we add it to our list
        n = n/p #then divide by p and we move onto getting our next number
      else: #when 2 no longer works as a prime factor and we need different ones then 1 gets added to p and we get more terms for the list
        p = p+1
    else:
      break
  return prime_factors #return the list of numbers


