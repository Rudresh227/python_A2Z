nums = [4,1,2,1,2]
dict = {}

for num in nums:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

for key,value in dict.items():
    if value == 1:
        print(key)
        break
