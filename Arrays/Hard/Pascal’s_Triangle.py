nums =[[1]]
rows = 6

for i in range(1,rows):
    row = [1]
    for j in range(1, i):
        row.append(nums[i - 1][j - 1] + nums[i - 1][j])

    row.append(1)
    nums.append(row)

print(nums)
