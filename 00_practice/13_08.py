from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for c in coins:
            if (a - c) >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    if dp[amount] != amount + 1:
        return dp[amount]
    else:
        return -1

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

coins = [2]
amount = 3
print(coinChange(coins, amount))

coins = [1,3,4,5]
amount = 7
print(coinChange(coins, amount))