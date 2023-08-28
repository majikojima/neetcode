from typing import List

def missingNumber(nums: List[int]) -> int:
    res = len(nums)
    for i in range(len(nums)):
        res += i - nums[i]
    return res

nums = [3,0,1]
print(missingNumber(nums))

nums = [0,1,2,3]
print(missingNumber(nums))