nums = [1,2,3,-3,1,1,1,4,2,-3]
prefix_sum = 0
count = 0
target = 3
dict = {0: 1}

for i in range(len(nums)):
    prefix_sum += nums[i]

    diff = prefix_sum - target
    if diff in dict:
        count += dict[diff]

    if prefix_sum in dict:
        dict[prefix_sum] += 1
    else:
        dict[prefix_sum] = 1

print(count)