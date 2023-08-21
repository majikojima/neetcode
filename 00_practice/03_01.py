from typing import List

def maxProfit(prices: List[int]) -> int:
    maxp = 0
    minp = 10000
    for price in prices:
        if price < minp:
            minp = price
        maxp = max(maxp, price - minp)
    return maxp

prices = [7,1,5,3,6,4]
print(maxProfit(prices))