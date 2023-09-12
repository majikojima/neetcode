from typing import List

def findTargetSumWays(nums: List[int], target: int) -> int:
    dp = {}  # (index, total) -> # of ways

    def backtrack(i, total):
        if i == len(nums):
            return 1 if total == target else 0
        if (i, total) in dp:
            return dp[(i, total)]

        dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
            i + 1, total - nums[i]
        )
        return dp[(i, total)]

    return backtrack(0, 0)

nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums, target))

"""
このコードは、与えられた数値のリスト`nums`とターゲット`target`が与えられたとき、各数値に+または-の記号をつけることで、数値の合計が`target`になる組み合わせの数を求めるものです。

具体的には以下のようになります：

1. **dp**: このディクショナリはメモ化のためのものです。キーは`(index, total)`として、あるインデックスの数値までで特定の合計を持つ方法の数を保存します。

2. **backtrack関数**:
    - **引数**:
        - `i`: 現在の数値のインデックス。
        - `total`: 現在の合計。
    - **処理**:
        - `i`が`nums`の長さに等しい場合（すべての数値を検討した場合）、合計がターゲットに等しいかどうかを確認して、結果を返します。
        - メモ化ディクショナリ`dp`に現在の`i`と`total`の組み合わせが存在する場合、その値を返します。
        - そうでない場合、現在の数値を合計に加える方法（+記号を使用）と、現在の数値を合計から減算する方法（-記号を使用）の2つの方法を再帰的に検討します。
        - 最後に、求めた方法の数をメモ化ディクショナリ`dp`に保存して返します。

3. 最後に、`backtrack`関数を初期値（0のインデックスと0の合計）で呼び出して、結果を返します。

このアプローチは、バックトラッキングの原則を使用して、各ステップで可能なすべての組み合わせを検討します。しかし、同じ組み合わせを複数回計算することを避けるために、メモ化を使用しています。
"""