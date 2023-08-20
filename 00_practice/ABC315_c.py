# [https://atcoder.jp/contests/abc315/tasks/abc315_c]
n = int(input())
bk = [[] for _ in range(n + 1)]

for _ in range(n):
    f, s = map(int, input().split())
    bk[f].append(s)

res = 0
best = []

for b in bk[1:]:
    b.sort(reverse=True)
    if len(b) >= 2:
        res = max(res, b[0] + b[1] // 2)
    if b:
        best.append(b[0])

best.sort(reverse=True)
if len(best) >= 2:
    res = max(res, best[0] + best[1])

print(res)

