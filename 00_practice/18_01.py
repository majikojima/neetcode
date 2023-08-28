from typing import List

def singleNumber(nums: List[int]) -> int:
    res = 0
    for n in nums:
        res = n ^ res
    return res

nums = [4,1,2,2,1]
print(singleNumber(nums))

nums = [2,2,1]
print(singleNumber(nums))