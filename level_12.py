from math import sqrt, ceil
triangle_number = 0
n = 1
while True:
    count = 2
    triangle_number += n  # every iteration of the looph as our triangle num increase by i
    # we check up to the sqrt of triangle_number because for every divisor there is below the sqrt there is one above it
    for i in range(1, ceil(sqrt(triangle_number))):
        # think of 100 to understand this concept
        if triangle_number % i == 0:
            count += 2
    if count > 500:
        print(triangle_number)
        break
    n += 1  # n increases by 1 every iteratiob of the loop 