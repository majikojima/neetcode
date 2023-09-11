from typing import List
import collections
import heapq

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))

times = [[1,2,1]]
n = 2
k = 1
print(networkDelayTime(times, n, k))

times = [[1,2,1]]
n = 2
k = 2
print(networkDelayTime(times, n, k))