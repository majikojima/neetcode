from typing import List

def search(nums: List, target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            return m
    return -1

nums = [5]
target = 5
# nums = [-1,0,3,5,9,12]
# target = 9
print(search(nums, target))