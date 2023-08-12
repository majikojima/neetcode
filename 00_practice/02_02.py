from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    print(f"numbers:\n {numbers}")
    print(f"target: {target}")

    while l < r:
        curSum = numbers[l] + numbers[r]
        print(f"l: {l}, r: {r}, curSum: {curSum}")
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l+1, r+1]
    return []

numbers = [2,7,11,15]
target = 18
print(twoSum(numbers, target))