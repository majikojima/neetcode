from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:

        
matrix = [[1]]
target = 2
print(searchMatrix(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))

target = 13
print(searchMatrix(matrix, target))