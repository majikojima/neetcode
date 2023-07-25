from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
            
        return res

s = Solution()

prices = [7,1,5,3,6,4]

result = s.maxProfit(prices)
print(result)

"""
このコードは、株価のリストが与えられた場合に、最大の利益を計算するためのものです。1行ずつ説明していきます。

1. `def maxProfit(self, prices: List[int]) -> int:`：`maxProfit`という名前の関数を定義しています。この関数は整数のリスト(`prices`)を引数にとり、整数を返します。

2. `res = 0`：利益を表す変数`res`を0で初期化しています。

3. `lowest = prices[0]`：最小の価格を表す変数`lowest`を、リスト`prices`の最初の要素で初期化しています。

4. `for price in prices:`：リスト`prices`の各要素（価格）についてループを回します。

5. `if price < lowest:`：現在見ている価格がこれまでの最低価格よりも低い場合、

6. `lowest = price`：その価格を新たな最低価格として更新します。

7. `res = max(res, price - lowest)`：現在の価格と最低価格との差（つまり売買した場合の利益）と、これまでの最大利益とを比較し、大きい方を新たな最大利益として更新します。

8. `return res`：計算した最大利益を返します。

このアルゴリズムは、価格リストを一度だけスキャンして最大利益を求めるので、効率的に解を見つけることができます。
"""

"""
もちろんです！この問題を考える際、株の売買を「お店でおもちゃを買う」という状況に置き換えて考えてみましょう。

あなたがお店で一番安い日におもちゃを買い、一番高い日にそれを売りたいと思っているとしましょう。ただし、買うのは1回だけで、売るのも1回だけです。そして、買った後に売るという順序が守られなければなりません。

毎日、お店に行っておもちゃの価格をチェックします。その日の価格がこれまで見た中で一番安ければ、それをメモします。これが「lowest = min(lowest, price)」の部分です。次に、その日の価格とメモした最安値との差（つまり、その日におもちゃを売った場合の利益）を計算し、それがこれまでの最大利益よりも大きければ、最大利益を更新します。これが「res = max(res, price - lowest)」の部分です。

つまり、このプログラムは「おもちゃの価格を毎日チェックし、最安値をメモしておき、それを基に最大利益を更新していく」というアルゴリズムを実装しているのです。
"""