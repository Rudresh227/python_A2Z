class Solution:
    def twoSum(self, numbers, target: int):
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]

            if total < target:
                left += 1

            else:
                right -= 1

sol = Solution()
example_input = [2,7,11,15]
result = sol.twoSum(example_input, 9)
print(result)