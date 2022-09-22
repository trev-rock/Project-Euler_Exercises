from itertools import permutations
permutations_list = list(permutations(range(0,10))) # permutations method generates all the perumations of that range, we need to put it in a list to iterate through all of them
s = [str(i) for i in permutations_list[999999]] # we want to get a string of all the numbers in the numbers
print(int("".join(s))) # put them all together and convert to an int for our final answer