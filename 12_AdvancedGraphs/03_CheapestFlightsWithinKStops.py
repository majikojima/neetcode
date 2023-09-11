from typing import List

def findCheapestPrice(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    prices = [float("inf")] * n
    prices[src] = 0

    for i in range(k + 1):
        tmpPrices = prices.copy()

        for s, d, p in flights:  # s=source, d=dest, p=price
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < tmpPrices[d]:
                tmpPrices[d] = prices[s] + p
        prices = tmpPrices
    return -1 if prices[dst] == float("inf") else prices[dst]

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(findCheapestPrice(n, flights, src, dst, k))

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print(findCheapestPrice(n, flights, src, dst, k))

"""
このコードは、空港のネットワークの中で特定のステップ数以内に目的地に到達する最も安い価格を探す問題のためのものです。具体的には、Bellman-Ford アルゴリズムを使用しています。

**大まかな説明**:
このアルゴリズムは、最初にすべての空港の価格を無限大に設定し、出発地の価格を0に設定します。次に、各ステップで各フライトの情報を使用して価格を更新します。これをk + 1回（指定されたステップ数）繰り返します。最後に、目的地の価格が更新されていればその価格を、そうでなければ-1を返します。

**部分毎の説明**:

1. `prices = [float("inf")] * n`: 
    - 各空港の価格を無限大に初期化します。

2. `prices[src] = 0`: 
    - 出発地の価格を0に設定します。

3. `for i in range(k + 1):`
    - 最大 k + 1回のステップで価格を更新します。

4. `tmpPrices = prices.copy()`: 
    - 現在の価格の一時的なコピーを作成します。これは、次のステップでの価格の更新に使用されます。

5. `for s, d, p in flights:`: 
    - すべてのフライト情報をループ処理します。

6. `if prices[s] == float("inf"):`
    - もし出発空港の価格が無限大であれば、このフライトは考慮外とします。

7. `if prices[s] + p < tmpPrices[d]:`
    - もし現在の出発空港からの価格にフライトの価格を加えたものが、目的地の一時的な価格よりも低ければ、価格を更新します。

8. `prices = tmpPrices`:
    - 一時的な価格を正式な価格に更新します。

9. `return -1 if prices[dst] == float("inf") else prices[dst]`:
    - 目的地の価格が無限大であれば、そのようなフライトの経路は存在しないため-1を返します。それ以外の場合は、計算された価格を返します。
"""