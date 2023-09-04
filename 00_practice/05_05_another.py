from typing import List

def search(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        
        # left sorted
        if nums[l] <= nums[m]:
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        # right sorted
        else:
            if nums[m] <= target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))

nums = [5,1,2,3,4]
target = 1
print(search(nums, target))

nums = [5,1,3]
target = 3
print(search(nums, target))