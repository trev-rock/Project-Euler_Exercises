import fractions # using this library so we can pull the denominator from our final fraction and also have a final fraction instead of a decimal

nums = [] # this list will hold our final fractions
for i in range (11,99): # we can have 11/12 as our lowest for both and 98/99 as the highest
    for j in range(i+1,100): # our range is i+1 because we need our fraction to always be less than 1
        # the numerator and denominator are being called top/bot in this because numerator and denominator are keywords 
        top, bot = list(str(i)), list(str(j)) # convert to a string then a list so we can easily take out the common digits 

        if top[1] == bot[0]: # we need to check if the ones place of the numerator matches the tens place of the denominator 
            top.pop(1) # remove the like numbers 
            bot.pop(0)
            top, bot = int(''.join(top)), int(''.join(bot))
            try: # use try and except in order avoid having errors 
                if top/bot == i/j: # compare the fractions 
                    nums.append([i,j])
            except:
                continue # we skip over anything that would cause errors like dividing by 0, for example 19/90 would cause this

        else:
            continue

product = 1 # we use 1 as a starting point similar to using 0 for sums 
for k in nums: # iterate through our list and multiply the numbers together
    product *= fractions.Fraction(k[0],k[1])

product = fractions.Fraction(product)
print(product.denominator)
