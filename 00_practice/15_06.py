from typing import List

def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:

triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]
print(mergeTriplets(triplets, target))

triplets = [[3,4,5],[4,5,6]]
target = [3,2,5]
print(mergeTriplets(triplets, target))
