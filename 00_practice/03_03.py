def characterReplacement(s: str, k: int) -> int:
    count = {}
    l = 0
    maxf = 0
    for r in range(len(s)):
        print(f"r: {r}")
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        print(f"count: {count}, maxf: {maxf}")
        print(f"(r - l + 1) - maxf: {(r - l + 1) - maxf}, k: {k}")
        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
            print(f"count: {count}, l: {l}")
        print(f"(r - l + 1): {(r - l + 1)}")
    return (r - l + 1)

s = "AABABBA"
k = 1
print(characterReplacement(s, k))

"""
r: 0
count: {'A': 1}, maxf: 1
(r - l + 1) - maxf: 0, k: 1
(r - l + 1): 1
r: 1
count: {'A': 2}, maxf: 2
(r - l + 1) - maxf: 0, k: 1
(r - l + 1): 2
r: 2
count: {'A': 2, 'B': 1}, maxf: 2
(r - l + 1) - maxf: 1, k: 1
(r - l + 1): 3
r: 3
count: {'A': 3, 'B': 1}, maxf: 3
(r - l + 1) - maxf: 1, k: 1
(r - l + 1): 4
r: 4
count: {'A': 3, 'B': 2}, maxf: 3
(r - l + 1) - maxf: 2, k: 1
count: {'A': 2, 'B': 2}, l: 1
(r - l + 1): 4
r: 5
count: {'A': 2, 'B': 3}, maxf: 3
(r - l + 1) - maxf: 2, k: 1
count: {'A': 1, 'B': 3}, l: 2
(r - l + 1): 4
r: 6
count: {'A': 2, 'B': 3}, maxf: 3
(r - l + 1) - maxf: 2, k: 1
count: {'A': 2, 'B': 2}, l: 3
(r - l + 1): 4
4
"""