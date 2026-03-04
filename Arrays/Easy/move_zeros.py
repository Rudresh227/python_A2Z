def moveZeroes(nums):
    non_zero_index = 0

    for num in nums:
        if num != 0:
            nums[non_zero_index] = num
            non_zero_index += 1

    for i in range(non_zero_index, len(nums)):
        nums[i] = 0

    return nums



nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

# Example 2:
nums2 = [0]
moveZeroes(nums2)
print(nums2)  # Output: [0]