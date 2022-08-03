def pentag(n):
    return (n * (3*n-1))/2


pentag_nums = [] 
possible_sols = []

for n in range(1,10001):
    pentag_nums.append(pentag(n))
    print(pentag(n))

for num in pentag_nums:
    for num2 in pentag_nums:
        print(num, num2)
        if num2 + num in pentag_nums and num2 - num in pentag_nums:
            print(f"{num}, {num2}, and lastly {num + num2}")
            possible_sols.append(num + num2)

print(possible_sols)