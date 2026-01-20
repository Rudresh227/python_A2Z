def maxSubArray(nums):
    # Initialize variables
    current_sum = 0
    max_sum = float('-inf')  # Start with the smallest possible value

    # Iterate through the array
    for num in nums:
        current_sum += num  # Add the current number to current_sum

        # Update max_sum if current_sum is greater
        if current_sum > max_sum:
            max_sum = current_sum

        # If current_sum drops below 0, reset it
        if current_sum < 0:
            current_sum = 0

    return max_sum



# Test case 1
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums1))  # Output: 6

# Test case 2
nums2 = [1]
print(maxSubArray(nums2))  # Output: 1

# Test case 3
nums3 = [5, 4, -1, 7, 8]
print(maxSubArray(nums3))  # Output: 23
