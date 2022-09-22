nums = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
        ] # our given numbers

sum = 0 # sum for the end

while len(nums) > 1: # we are going to be reducing the length of the overall list of numbers until we have one final
    examine = nums[-2] # we want to look at the second to last row
    temp = [] # this list will hold all of the greatest sums we can make between the second to last row and last row
    for i in examine: # looking through the second to last row
        index = examine.index(i) # get the index of each number because we need to either look at the number of equal index (or left of it) to it in the next row or the number to its right 
        # based on which number below the current one we are looking at, whichever is larger we will add to it then add it to our temp list
        if nums[-1][index] >= nums[-1][index+1]: 
            j = i + nums[-1][index]
            temp.append(j)
        elif nums[-1][index] <= nums[-1][index+1]:
            j = i + nums[-1][index+1]
            temp.append(j)
    # after we go through the rows and add everything into our temp list we remove the two rows and add in the temp one we just had
    nums.pop()
    nums.pop()
    nums.append(temp)
print(nums[0][0]) # print our final result