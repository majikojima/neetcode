from typing import List
import collections

def orangesRotting(grid: List[List[int]]) -> int:
    

grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
print(orangesRotting(grid))

grid = [[0,2]]
print(orangesRotting(grid))