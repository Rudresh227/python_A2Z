'''
Input: nums = [3,4,5,1,2]
Output: true

Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
'''

count = 0
nums = [4,1,2,3,6,5]

for i in range(len(nums)):
    if nums[i] > nums[(i + 1) % len(nums)]:
        count += 1

if count > 1:
    print("False")
else:
    print("True")


