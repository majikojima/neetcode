from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

    def add(self, val: int) -> int:

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3));   # return 4
print(kthLargest.add(5));   # return 5
print(kthLargest.add(10));  # return 5
print(kthLargest.add(9));   # return 8
print(kthLargest.add(4));   # return 8