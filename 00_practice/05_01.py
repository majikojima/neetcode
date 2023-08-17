from typing import List

def search(nums: List[int], target: int) -> int:
    print(f"nums: {nums}, target: {target}")
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        print(f"m: {m}, nums: {nums[m]}")
        m = l + (r - l) // 2
        print(f"m: {m}, nums: {nums[m]}")
        if target < nums[m]:
            r = m - 1
        elif target > nums[m]:
            l = m + 1
        else:
            return m
    return -1

nums = [-10,-5,-3,-1,0,3,5,9,12,13,14,15]
target = 9
print(search(nums, target))

target = -5
print(search(nums, target))