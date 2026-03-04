'''
https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
'''
from sys import prefix

nums = [10,5,2,7,1,-10]
k = 15

dict = {0:-1}
prefix = 0
max_len = 0

for i in range(len(nums)):
    prefix += nums[i]

    if prefix - k in dict:
        max_len = max(max_len, i - dict[prefix - k])

    dict[prefix] = i

print(max_len)