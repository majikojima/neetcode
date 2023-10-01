def Fes(N, M, A):
    res = [0] * N
    Aset = set(A)

    for day in range(N - 1, -1, -1):
        if (day + 1) in Aset:
            lastDay = day + 1
        res[day] = lastDay - (day + 1)

    for n in res:
        print(n)

    return

N, M = map(int, input().split())
A = list(map(int, input().split()))

Fes(N, M, A)

# LTE

# def Fes(N, M, A):
#     res = [0] * N
#     Aset = set(A)

#     for i in range(N):
#         day = i + 1
#         dif = 0
#         while day < N and day not in Aset:
#             day += 1
#             dif += 1
#         res[i] = dif

#     for n in res:
#         print(n)

#     return