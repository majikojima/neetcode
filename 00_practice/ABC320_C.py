# [https://atcoder.jp/contests/abc320/tasks/abc320_c]
def find_minimum_seconds(M, S1, S2, S3):
    res = float("inf")

    for t1 in range(M*3):
        for t2 in range(M*3):
            if t1 == t2:
                continue
            for t3 in range(M*3):
                if t1 == t3 or t2 == t3:
                    continue
                if S1[(t1 % M)] == S2[(t2 % M)] == S3[(t3 % M)]:
                    res = min(res, max(t1, t2, t3))

    return res if res != float('inf') else -1

M = int(input())
S1 = input()
S2 = input()
S3 = input()
print(find_minimum_seconds(M, S1, S2, S3))