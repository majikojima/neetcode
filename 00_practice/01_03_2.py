from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return None

nums = [2,7,11,15]
target = 26

print(twoSum(nums, target))