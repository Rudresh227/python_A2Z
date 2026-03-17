nums = [1,0,-1,0,-2,2]
target = 0

nums.sort()  # Step 1: Sort the array
n = len(nums)
result = set()  # Step 2: Use a set to avoid duplicates

for i in range(n - 3):

    for j in range(i + 1, n - 2):

        left, right = j + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[j] + nums[left] + nums[right]

            if current_sum == target:
                result.add((nums[i], nums[j], nums[left], nums[right]))

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

# Convert the set of tuples to a list of lists
print([list(quad) for quad in result])