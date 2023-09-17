# [https://atcoder.jp/contests/abc320/tasks/abc320_a]

A, B = map(int, input().split())

res = pow(A, B) + pow(B, A)
print(res)