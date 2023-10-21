N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

res = 0
for i in range(0, N - M):
    res += (A[i] + A[(N - M) * 2 - i - 1]) ** 2

for i in range((N - M) * 2, N):
    res += A[i] ** 2

print(res)