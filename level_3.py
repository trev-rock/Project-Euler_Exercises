num = 600851475143  # the number we want to find the factors of
p = 3  # start with 3 because 1 is not a prime number and 2 is not a factor since num is odd
factors = []  # our list of factors
while num > 1:  # it will continuously decrease for prime factorization
    if num >= p:
        if num % p == 0:  # if p is a multiple of num then add it to our list
            factors.append(p)
            num /= p  # divide by p, this is part of prime factorization
        else:  # if it is not divisible by p then add 1 to p until the next term is found
            p += 1
print(max(factors))
