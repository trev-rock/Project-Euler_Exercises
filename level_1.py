total = 0  # starting point for our sum at the end
for i in range(0, 1000):  # want to know for all i under 1000
    if i % 3 == 0 or i % 5 == 0:  # if a i % 3 or 5 == 0 then we know it is a mnultiple of i
        total += i  # add it to the sum at the end
print(total)
