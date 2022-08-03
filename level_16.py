nums = list(str(2**1000)) # find 2^1000, make it into a string and put each character into an index of a list
for i in range(len(nums)): # convert each value into an integer
  nums[i] = int(nums[i])
print(sum(nums)) # find their sum