nums = [1,2,3,4]

n = len(nums)
result = [1] * n

# Step 1: Fill result with prefix products
prefix = 1
for i in range(n):
    result[i] = prefix
    prefix *= nums[i]

# Step 2: Multiply suffix products directly into result
suffix = 1
for i in range(n - 1, -1, -1):
    result[i] *= suffix
    suffix *= nums[i]

print(result)