from typing import List
import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    minHeap = []
    for x, y in points:
        distance = (x ** 2) + (y ** 2)
        minHeap.append((distance, x, y))
    heapq.heapify(minHeap)

    res = []
    for _ in range(k):
        _, x, y = heapq.heappop(minHeap)
        res.append((x, y))
    return res

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))