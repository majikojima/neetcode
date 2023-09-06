from collections import deque, Counter
from typing import List
import heapq

def leastInterval(tasks: List[str], n: int) -> int:

        
tasks = ["A","A","A","B","B","B"]
n = 2
print(leastInterval(tasks, n))
        
tasks = ["A","A","A","B","B","C","C"]
n = 2
print(leastInterval(tasks, n))