nums = [1,2,3,7,8,6,9]

first = float('-inf')
second = float('-inf')

for num in nums:
    if num > first:
        second = first
        first = num

    elif num > second and num < first:
        second = num

print(second)