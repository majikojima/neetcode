from typing import List

def countBits(n: int) -> List[int]:
    dp = [0] * (n + 1)
    offset = 1
    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp

n = 17
print(countBits(n))