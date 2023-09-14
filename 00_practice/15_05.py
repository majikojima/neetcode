from typing import List
import heapq

def isNStraightHand(hand: List[int], groupSize: int) -> bool:

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(isNStraightHand(hand, groupSize))

hand = [1,2,3,4,5]
groupSize = 4
print(isNStraightHand(hand, groupSize))