import collections

def RoundRobinTournament(N, S) -> list[int]:
    winMap = collections.defaultdict(list)
    for i, s in enumerate(S):
        win = 0
        for c in s:
            if c == "o":
                win += 1
        winMap[win].append(i)
    
    res = []
    for i in sorted(winMap.keys(), reverse=True):
        for n in winMap[i]:
            res.append(n+1)
    return ' '.join(map(str, res))

N = int(input())
S = [None] * N
for i in range(N):
    S[i] = input()
print(RoundRobinTournament(N, S))