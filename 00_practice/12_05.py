from typing import List
import heapq

def swimInWater(grid: List[List[int]]) -> int:
    

grid = [
    [0,2],
    [1,3]
]
print(swimInWater(grid))

grid = [
    [0,1,2,3,4],
    [24,23,22,21,5],
    [12,13,14,15,16],
    [11,17,18,19,20],
    [10,9,8,7,6]
]
print(swimInWater(grid))