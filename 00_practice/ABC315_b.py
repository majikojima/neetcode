# [https://atcoder.jp/contests/abc315/tasks/abc315_b]
import numpy as np
M = int(input())
D = list(map(int, input().split()))
t = np.sum(D) // 2

for i,n in enumerate(D):
    if t // n == 0:
        print(i + 1, t % n + 1)
        break
    t -= n