def findDuplicate(nums):
    hashmap = {}
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            return num

print(findDuplicate([1, 3, 4, 2, 2]))  # Expected: 2
print(findDuplicate([3, 1, 3, 4, 2]))  # Expected: 3
print(findDuplicate([1, 1]))           # Expected: 1
print(findDuplicate([1, 2, 3, 4]))     # Expected: -1 (no duplicate)


#Optimal
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
