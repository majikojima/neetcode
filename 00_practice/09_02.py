from typing import List
import heapq

def lastStoneWeight(stones: List[int]) -> int:
    maxHeap = [-s for s in stones]
    heapq.heapify(maxHeap)
    while len(maxHeap) > 1:
        y = heapq.heappop(maxHeap)
        x = heapq.heappop(maxHeap)
        if x != y:
            heapq.heappush(maxHeap, y - x)
    if len(maxHeap) == 1:
        return -heapq.heappop(maxHeap)
    else:
        return 0

stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones))