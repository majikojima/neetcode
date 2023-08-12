from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            print(prevMap)

s = Solution()

nums = [2,7,11,15]
target = 26

result = s.twoSum(nums, target)
print(result)
