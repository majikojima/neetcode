from typing import List

def findMin(nums: List[int]) -> int:
    res = nums[0]
    l = 0
    r = len(nums) - 1
    while l <= r:
        if nums[l] <= nums[r]:
            res = min(res, nums[l])
            break
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[l] <= nums[m]:
            l = m + 1
        else:
            r = m - 1
    return res


nums = [3,4,5,1,2]
print(findMin(nums))