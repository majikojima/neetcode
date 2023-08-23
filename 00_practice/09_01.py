from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3);   # return 4
kthLargest.add(5);   # return 5
kthLargest.add(10);  # return 5
kthLargest.add(9);   # return 8
kthLargest.add(4);   # return 8