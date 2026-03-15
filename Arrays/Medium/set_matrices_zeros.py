#Brute Force
matrix = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

def markRow(i):
    for j in range(len(matrix[0])):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(j):
    for i in range(len(matrix)):
        if matrix[i][j] != 0:
            matrix[i][j] = -1


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            markRow(i)
            markCol(j)
print('Initial',matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == -1:
            matrix[i][j] = 0
print('Final',matrix)


#Better
matrix = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

row = [0] * len(matrix)
col = [0] * len(matrix[0])

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            row[i] = 1
            col[j] = 1

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if (row[i] == 1 or col[j] == 1):
            matrix[i][j] = 0
print(matrix)

#Optimal
matrix = [[1,1,1,1],[0,1,0,1],[1,1,0,1],[1,1,1,1]]

col0 = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            matrix[i][0] = 0

            if j != 0:
                matrix[0][j] = 0
            else:
                col0 = 0

for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0

if matrix[0][0] == 0:
    for i in range(len(matrix[0])):
        matrix[0][i] = 0

if col0 == 0:
    for i in range(len(matrix)):
        matrix[i][0] = 0
print('Optimal', matrix)
