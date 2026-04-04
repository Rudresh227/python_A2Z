from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row, col = len(matrix), len(matrix[0])
    top = 0
    bottom = row - 1
    while top <= bottom:
        row_idx = (top + bottom) // 2
        if target < matrix[row_idx][0]:
            bottom = row_idx - 1
        elif target > matrix[row_idx][-1]:
            top = row_idx + 1
        else:
            break

    if not (top <= bottom):
        return False

    left = 0
    right = col - 1

    while left <= right:
        col_idx = (left + right) // 2
        if target < matrix[row_idx][col_idx]:
            right = col_idx - 1
        elif target > matrix[row_idx][col_idx]:
            left = col_idx + 1
        else:
            return True
    return False


matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
print(searchMatrix(matrix1, 3))   # True
print(searchMatrix(matrix1, 13))  # False

matrix2 = [[1]]
print(searchMatrix(matrix2, 1))   # True
print(searchMatrix(matrix2, 2))   # False