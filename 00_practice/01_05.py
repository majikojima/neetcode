from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for _ in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    for n, c in count.items():
        freq[c].append(n)
    print(freq)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

nums = [1,1,1,2,3,3,3,4]
k = 2

result = topKFrequent(nums, k)
print(result)

"""
count: {1: 2}
count: {1: 3}
count: {1: 4}
count: {1: 4, 2: 2}
count: {1: 4, 2: 2, 3: 2}
count: {1: 4, 2: 2, 3: 3}
count: {1: 4, 2: 2, 3: 4}
count: {1: 4, 2: 2, 3: 4, 4: 2}
freq: [[], [], [], [], [], [], [], [], []]
n: 1, c: 4, freq: [[], [], [], [], [1], [], [], [], []]
n: 2, c: 2, freq: [[], [], [2], [], [1], [], [], [], []]
n: 3, c: 4, freq: [[], [], [2], [], [1, 3], [], [], [], []]
n: 4, c: 2, freq: [[], [], [2, 4], [], [1, 3], [], [], [], []]
i: 8, freq[i]: []
i: 7, freq[i]: []
i: 6, freq[i]: []
i: 5, freq[i]: []
i: 4, freq[i]: [1, 3]
n: 1
n: 3
[1, 3]
"""