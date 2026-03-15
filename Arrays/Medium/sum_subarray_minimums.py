'''
Input : arr[] = [4, 3, 1, 5, 6]
Output : 11
Explanation : Subarrays with smallest and second smallest are:- [4, 3] smallest = 3,second smallest = 4
[4, 3, 1] smallest = 1, second smallest = 3
[4, 3, 1, 5] smallest = 1, second smallest = 3
[4, 3, 1, 5, 6] smallest = 1, second smallest = 3
[3, 1] smallest = 1, second smallest = 3
[3, 1, 5] smallest = 1, second smallest = 3
[3, 1, 5, 6] smallest = 1, second smallest = 3
[1, 5] smallest = 1, second smallest = 5
[1, 5, 6] smallest = 1, second smallest = 5
[5, 6] smallest = 5, second smallest = 6
Maximum sum among all above choices is, 5 + 6 = 11.
'''

'''
#Brute Force
arr = [3, 1, 2, 4]
final = 0

for i in range(len(arr)):
    minimum = float('inf')
    for j in range(i, len(arr)):
        if arr[j] < minimum:
            minimum = arr[j]
        final += minimum

print(final)
'''

#Optimal

arr = [1,4,6,7,3,7,8,1]
left = [0] * len(arr)
right = [0] * len(arr)
MOD = (10 ** 9) + 7
stack = []
for i in range(len(arr)):
    count = 1
    while stack and stack[-1][0] > arr[i]:
        count += stack.pop()[1]
    stack.append([arr[i],count])
    left[i] = count

stack = []
for i in range(len(arr) - 1, -1, -1):
    count = 1
    while stack and stack[-1][0] >= arr[i]:
        count += stack.pop()[1]
    stack.append([arr[i],count])
    right[i] = count

total = 0
for i in range(len(arr)):
    total += left[i] * right[i] * arr[i]

print(total % MOD)

