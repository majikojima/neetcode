from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    cost = cost[::-1]
    for i in range(2, len(cost), 1):
        cost[i] += min(cost[i-1], cost[i-2])
        
    cost = cost[::-1]
    return min(cost[0], cost[1])

cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))