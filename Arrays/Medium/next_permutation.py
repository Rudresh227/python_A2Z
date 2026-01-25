'''
LeetCode Problem: Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order,
then the next permutation of that array is the permutation that follows it in the sorted container.

If such an arrangement is not possible, the array must be rearranged as the lowest possible order
(i.e., sorted in ascending order).

You must do this in-place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

'''

#Optimal
import sys
nums = [2,1,5,4,3,0,0]
# nums = [5,4,3,2,1]

index = -1

for i in range(len(nums) - 2, -1, -1):
    if nums[i] < nums[i + 1]:
        index = i
        break

if index == -1:
    print(sorted(nums))
    sys.exit()

for i in range(len(nums) - 1, index, -1):
    if nums[i] > nums[index]:
        nums[index], nums[i] = nums[i], nums[index]
        break

sort_result = nums[:index + 1] + sorted(nums[index + 1:])
print(sort_result)



