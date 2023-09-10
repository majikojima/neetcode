from typing import List

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses, prerequisites))

numCourses = 6
prerequisites = [[0,1],[0,2],[1,3],[3,2],[4,0],[5,0]]
print(findOrder(numCourses, prerequisites))