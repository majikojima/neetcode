def climbStairs(n: int) -> int:
    if n <= 3:
        return n
    n1 = 2
    n2 = 3
    for _ in range(4, n+1):
        res = n1 + n2
        n1 = n2
        n2 = res
    return res

n = 5
print(climbStairs(n))