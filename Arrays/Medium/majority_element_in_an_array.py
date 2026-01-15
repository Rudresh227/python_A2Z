class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        # First pass: Find the candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # Optional: Verify the candidate (second pass)
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) // 2:
            return candidate
        else:
            return -1  # No majority element if count is not > n // 2


# Example usage:
sol = Solution()
nums = [3, 2, 3]
result = sol.majorityElement(nums)
print(result)  # Output will be 3 (majority element)
