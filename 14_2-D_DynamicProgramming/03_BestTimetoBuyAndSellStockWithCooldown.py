from typing import List

def maxProfit(self, prices: List[int]) -> int:
    # State: Buying or Selling?
    # If Buy -> i + 1
    # If Sell -> i + 2

    dp = {}  # key=(i, buying) val=max_profit

    def dfs(i, buying):
        if i >= len(prices):
            return 0
        if (i, buying) in dp:
            return dp[(i, buying)]

        cooldown = dfs(i + 1, buying)
        if buying:
            buy = dfs(i + 1, not buying) - prices[i]
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i + 2, not buying) + prices[i]
            dp[(i, buying)] = max(sell, cooldown)
        return dp[(i, buying)]

    return dfs(0, True)

prices = [1,2,3,0,2]
print(maxProfit(prices))

prices = [1]
print(maxProfit(prices))

"""
このコードは、株式の取引に関する問題を解決するものです。基本的なアイディアは、ある日に購入または売却することを選択でき、売却の後には1日のクールダウン期間が必要であるという点です。コードは、指定された価格のリストをもとに、可能な最大の利益を求めるものです。

コードの部分ごとの説明を行います：

1. **コメントと初期化**:
   ```python
   # State: Buying or Selling?
   # If Buy -> i + 1
   # If Sell -> i + 2

   dp = {}  # key=(i, buying) val=max_profit
   ```
   - `buying`の状態は、購入か売却かを示すものです。購入する場合、次の日には購入または売却することができます。売却する場合、次の日にはクールダウンが必要なため、次回の取引は2日後になります。
   - `dp`はメモ化のための辞書で、`i`日における`buying`状態の最大利益を保存します。

2. **再帰関数 `dfs`**:
   ```python
   def dfs(i, buying):
       ...
   ```
   この関数は、指定された日`i`での`buying`状態における最大の利益を計算するものです。

   - 基本ケース：`i`が`prices`の長さ以上の場合、`0`を返します。
   - メモ化の確認：`dp`にすでに値が格納されている場合、それを返します。
   - 購入または売却の場合に対応する処理を行い、結果を`dp`に保存します。

3. **最終的な結果の返却**:
   ```python
   return dfs(0, True)
   ```
   このコードは、0日目に購入する場合の最大利益を返します。このため、`dfs`関数を`i=0`、`buying=True`の状態で呼び出します。

このアルゴリズムはメモ化を使用しているので、時間計算量は`O(n)`、空間計算量も`O(n)`です（ここで`n`は`prices`の長さを指します）。
"""