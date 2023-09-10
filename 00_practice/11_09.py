from typing import List

def findRedundantConnection(edges: List[List[int]]) -> List[int]:

edges = [[1,2],[1,3],[2,3]]
print(findRedundantConnection(edges))

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(findRedundantConnection(edges))