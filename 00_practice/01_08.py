from typing import List

def longestConsecutive(nums: List[int]) -> int:
    res = 0
    numSet = set(nums)
    for n in numSet:
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            res = max(res, length)
    return res

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))