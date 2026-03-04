nums = [1,2,3,4,5]
k = 2

k = k % len(nums)

left, right = 0, len(nums) - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

left, right = 0, k - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

left, right = k, len(nums) - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

print(nums)
