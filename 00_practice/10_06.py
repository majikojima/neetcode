from collections import Counter, defaultdict
from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))

word = "SEE"
print(exist(board, word))

word = "ABCB"
print(exist(board, word))