"""
Problem: Two Sum

Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add up to target.


Example:
Input:
    nums = [2, 7, 11, 15]
    target = 9

Output:
    [0, 1]

Explanation:
    nums[0] + nums[1] = 2 + 7 = 9
"""


nums = [2,7,11,15]
target = 9

dict = {}

for i in range(len(nums)):
    diff = target - nums[i]

    if diff in dict:
        print(i, dict[diff])
        break

    dict[nums[i]] = i