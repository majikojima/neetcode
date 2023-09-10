from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    

numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))

numCourses = 5
prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]]
print(canFinish(numCourses, prerequisites))

numCourses = 3
prerequisites = [[0,1],[1,2],[2,0]]
print(canFinish(numCourses, prerequisites))