arr = [1,2,3,4,5,9,6,7,8]
maximum = float('-inf')

for num in arr:
    if num > maximum:
        maximum = num
print(maximum)