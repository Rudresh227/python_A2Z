matrix = [[1,  2,  3,  4,  5],
[16, 17, 18, 19, 6],
[15, 24, 25, 20, 7],
[14, 23, 22, 21, 8],
[13, 12, 11, 10, 9]]

left,right,top,bottom = 0, len(matrix) - 1, 0, len(matrix)- 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        print(matrix[top][i])
    top += 1

    for j in range(top, bottom + 1):
        print(matrix[j][right])
    right -= 1

    if not top <= bottom and left <= right:
         break

    for i in range(right, left - 1,-1):
        print(matrix[bottom][i])
    bottom -= 1

    for j in range(bottom, top - 1,-1):
        print(matrix[j][left])
    left += 1


