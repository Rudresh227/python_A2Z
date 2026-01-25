'''
Array Leaders Problem - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Given an array of integers, find all the leaders in the array.

An element is called a leader if it is greater than or equal to all the elements to its right side.
The rightmost element is always a leader.

Return the leaders in the same order as they appear in the array.

Example 1:
Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation:
- 17 is greater than all elements to its right.
- 5 is greater than 2.
- 2 is the rightmost element.

Example 2:
Input: arr = [1, 2, 3, 4, 0]
Output: [4, 0]

Constraints:
- 1 <= arr.length <= 10^5
- -10^9 <= arr[i] <= 10^9
'''

#Brute Force:
nums = [10,22,12,3,0,6]
result = []

for i in range(len(nums)):
    leader = True
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            leader = False
            break

    result.append(nums[i]) if leader == True else False
print(result)


#Optimal
arr = [10,22,12,3,0,6]

maxi = float('-inf')
result = []

for i in range(len(nums) - 1, -1, -1):
    if nums[i] > maxi:
        result.append(nums[i])
        maxi = max(nums[i], maxi)

result = result[::-1]

print(result)
