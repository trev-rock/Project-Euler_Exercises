a = 0  # very first term of sequence
b = 1  # second term of sequence
even_nums = []  # a list to store our even numbers
while b <= 4000000:  # we don't want to exceed 4 mil
    temp_a = a  # need a temporary value as we swap things around, this is because we are not using recursion
    a = b  # a always becomes the current value of b
    # we add the original values of a and b (of this iteration) together and this becomes our new b
    b = temp_a + b
    if b % 2 == 0:  # if it is even add it to the list
        even_nums.append(b)
print(sum(even_nums))
