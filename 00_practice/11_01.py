from typing import List

def numIslands(grid: List[List[str]]) -> int:
    

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))

grid = [["1"],["1"]]
print(numIslands(grid))