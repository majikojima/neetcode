from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for _ in range(len(nums))]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, -1, -1):
        while freq[i]:
            res.append(freq[i].pop())
            k -= 1
            if k == 0:
                return res
    return res


nums = [1,1,1,2,3,3,3,4]
k = 2

result = topKFrequent(nums, k)
print(result)
