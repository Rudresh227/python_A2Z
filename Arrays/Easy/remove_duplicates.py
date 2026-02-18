def removeDuplicates(nums):
    seen = {}
    count = 0

    for num in nums:
        if num not in seen:
            seen[num] = True
            nums[count] = num
            count += 1

    return count


# Example 1
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 2, nums = [1, 2]

# Example 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 5, nums = [0, 1, 2, 3, 4]
