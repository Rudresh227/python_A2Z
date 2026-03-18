import collections


def isValidSudoku(board):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    grid = collections.defaultdict(set)

    for r in range(len(board)):
        for c in range(len(board)):
            val = board[r][c]

            if val == '.':
                continue

            if val in rows[r]:
                return False
            rows[r].add(val)

            if val in cols[c]:
                return False
            cols[c].add(val)

            if val in grid[(r//3)*3 + (c//3)]:
                return False
            grid[(r//3)*3 + (c//3)].add(val)

    return True



# Test
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))  # True