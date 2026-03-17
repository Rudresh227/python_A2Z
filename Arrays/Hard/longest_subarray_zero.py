nums = [15, -2, 2, -8, 1, 7, 10, 23]

prefix_sum = 0
max_len = 0
dict = {0: -1}
target = 0

for i in range(len(nums)):
    prefix_sum += nums[i]

    diff = prefix_sum - target
    if diff in dict:
        max_len = max(max_len, i - dict[diff])

    if prefix_sum not in dict:
        dict[prefix_sum] = i

print(max_len)

