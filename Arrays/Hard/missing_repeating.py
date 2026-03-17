# GFG: https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1

#Using Formula
arr = [1,2,2,4]
n = 4
# Expected sums
S = n * (n + 1) // 2
P = n * (n + 1) * (2 * n + 1) // 6
print(S,P)

# Actual sums
S1 = sum(arr)
P1 = sum(x * x for x in arr)
print(S1, P1)

# Equations
diff = S - S1  # missing - repeated
sum_diff = (P - P1) // diff  # missing + repeated

missing = (diff + sum_diff) // 2
repeated = sum_diff - missing

print([repeated, missing])



#Using Hashmap
nums = [1,2,2,4]
dict = {}

for i in range(len(nums)):
    dict[i + 1] = 0

for num in nums:
    if num in dict:
        dict[num] += 1

repeating = None
missing = None

for key, value in dict.items():
    if value > 1:
        repeating = key
    if value < 1:
        missing = key

print('Missing: ',missing)
print('Repeating: ', repeating)