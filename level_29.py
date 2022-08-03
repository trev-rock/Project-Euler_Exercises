sett = set()
# we need 2 to be raised from the 2 power to 100, then 3 raised to the same, and so on, so this is why we have our nested for loops
# we add them to a set because a set will not take repeated values unlike a list
for a in range(2, 101):
    for b in range(2, 101):
        sett.add(a**b) # add it to the set, only unique values will be added so no repeats 
print(len(sett))
