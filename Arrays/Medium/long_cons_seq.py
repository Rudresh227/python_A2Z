nums = [100,5,200,1,2,3,4]


#Brute Force
nums = sorted(nums)
max_len = 0
count = 0

for i in range(1, len(nums)):
    if nums[i] == nums[i - 1] + 1:
        count += 1
    max_len = max(max_len, count)

print(max_len)

#Optimal
nums = set(nums)
max_streak = 1

for num in nums:
    if (num - 1) not in nums:
        streak = 1
        current_num = num
        while current_num + 1 in nums:
            streak += 1
            current_num += 1
        max_streak = max(streak, max_streak)

print(max_streak)
