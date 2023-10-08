def isEvenZero(S) -> bool:
    for i in range(len(S)):
        if i % 2 == 1:
            n = ord(S[i]) - ord("0")
            if n == 1:
                return False
    return True

S = input()
if isEvenZero(S):
    print("Yes")
else:
    print("No")
