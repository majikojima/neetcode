from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(canCompleteCircuit(gas, cost))

gas = [2,3,4]
cost = [3,4,3]
print(canCompleteCircuit(gas, cost))