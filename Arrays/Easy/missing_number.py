from werkzeug.debug.repr import missing

nums = [1,2,3,4,5,6,8]
n = len(nums) + 1

current_sum = 0
expected_sum = 0

expected_sum = n * (n + 1)//2

for num in nums:
    current_sum += num

missing_number = expected_sum - current_sum
print(missing_number)