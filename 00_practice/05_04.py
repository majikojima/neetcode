from typing import List

def findMin(nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]

nums = [3,4,5,1,2]
print(findMin(nums))