from math import prod # takes the product of a list
nums = list('7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450') # turn this 1000 digit number into a list so we can work with each number individually 
for y in range(len(nums)): # convert each number in the list from a string to an integer
  nums[y] = int(nums[y]) 
# we start with 0 and 12 from that starting point as our initial values because when we iterate through our list we will be working with 13 adjacent numbers 
start = 0
end = start + 12
products = [] 
while end != 1000: # if end reaches 1000 then we can no longer get 13 adjacent values 
  temp = [] # this temporary list will be what holds our 13 numbers
  for i in range(start,end+1): # we need to say "end + 1" so we can get all 13 digits 
    temp.append(nums[i]) # put the 13 adjacent numbers into the temp list 
  product = prod(temp) # take the product of the list
  products.append(product) # put it in our list of products
  start += 1 # iterate start and end to their next values, essentially shifting over to the next 13
  end += 1
  if len(products) == 2: # we say when the length is 2 because the next few lines can't run on the first iteration of this
    # these lines compare if if the new product is higher or lower than the previous one in the list, the lower value gets deleted
    if products[0] > products[1]:
      del products[1]
    elif products[1] > products[0]:
      del products[0]
    elif products[0] == products[1]:
      del products[1]

print(products[0]) # printing the final product