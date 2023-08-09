import collections
from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    # rows = [set() for _ in range(len(board))]
    # columns = [set() for _ in range(len(board))]
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    subs = collections.defaultdict(set)

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in columns[c]
                or board[r][c] in subs[(r // 3, c // 3)]
            ):
                return False
            rows[r].add(board[r][c])
            columns[c].add(board[r][c])
            subs[(r // 3, c // 3)].add(board[r][c])
            print(f"rows: {rows}")
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