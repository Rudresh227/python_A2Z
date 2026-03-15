#Brute Force
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
arr = [[0 for i in range(len(matrix))] for i in range(len(matrix))]

left = 0
right = len(matrix) - 1

for i in range(len(matrix)):
    for j in range(len(matrix)):
        arr[j][right] = matrix[i][j]
    right -= 1
print(arr)

#Optimal
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

for i in range(1,len(matrix)):
    for j in range(i):
        if i != j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(len(matrix)):
    left = 0
    right = len(matrix) - 1
    while left < right:
        matrix[i][left], matrix[i][right] = matrix[i][right],matrix[i][left]
        left += 1
        right -= 1

print(matrix)