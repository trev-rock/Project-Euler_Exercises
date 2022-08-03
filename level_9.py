# we want to iterate through these ranges because a cannot be higher than 331 in theory, b must be higher than a, in theory these ranges could probably be reduced even more
for a in range(1,332):
  for b in range(a+1,501):
    for c in range(1,501):
      if a**2 + b**2 == c**2 and a+b+c == 1000: # we want to check that it is a pythagorean triplet and that their sum is 1000
        print(a*b*c) # print the final product