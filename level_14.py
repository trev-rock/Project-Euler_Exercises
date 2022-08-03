seqs = [] # holds the length of each sequence in order, the index of the count is also the number used for that sequence to find the count 
for n in range(1, 1000000): # looking for the longest chain under 1 mil
    count = 1 # counter restarts every iteration
    # put in the starting value of n first as a key with no value then update its count at the end
    while True:
        if n == 1: # when the number is reduced to 1 we take the count and add it to our list containing all of the counts 
            seqs.append(count)
            break
        if n % 2 == 0: # if the current value of n is even then we divide by 2 and increase our count by 1
            n /= 2
            count += 1
        else: # if the current value of n is odd then we multiply it by 3 and add 1
            n = 3*n + 1
            count += 1


print(f"{seqs.index(max(seqs))+1}, {max(seqs)}") # use the + 1 because the indices start at 0
