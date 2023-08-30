import collections
from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    rows = collections.defaultdict(list)
    cols = collections.defaultdict(list)
    subs = collections.defaultdict(list)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in subs[(r//3, c//3)]
            ):
                return False
            rows[r].append(board[r][c])
            cols[c].append(board[r][c])
            subs[(r//3, c//3)].append(board[r][c])
    return True


board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

result = isValidSudoku(board)

print(result)