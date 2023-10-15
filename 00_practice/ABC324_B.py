def smooth():
    N = int(input())

    while N % 2 == 0:
        N //= 2

    while N % 3 == 0:
        N //= 3

    if N == 1:
        return True
    else:
        return False
    
if smooth():
    print("Yes")
else:
    print("No")