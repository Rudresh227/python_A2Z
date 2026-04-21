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
