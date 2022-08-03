num = 1  # our starting point
i = 1  # starting point for what to divide by
con = False
while con == False:  # just to make the loop infinite
    if num % i == 0:  # this is where we check if num is divisible by i
        if i == 20:  # if i is 20 then that means everything under it is also a factor of num
            print(num)
            con = True  # ends the loop
        else:
            i += 1  # iterate to the next value of i to see if it is also a factor of num
    else:
        i = 1  # reset i back to 1 to check for our next number
        num += 1  # if it wasn't divisible by all 20 then we move onto the next number
