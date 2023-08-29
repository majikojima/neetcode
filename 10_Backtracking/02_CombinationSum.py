from typing import List
import numpy as np

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res

candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))

"""
この関数は、与えられた候補のリスト`candidates`から数値を選び、その和が`target`となる全ての組み合わせを返すものです。数値は複数回選択できます。

大まかな説明:
関数`combinationSum`は、深さ優先探索（DFS）を利用して、組み合わせの和がターゲットに一致するか確認します。一致する組み合わせが見つかった場合、その組み合わせを結果リスト`res`に追加します。

部分ごとの説明:

1. `res = []`: 結果を格納する空のリストを初期化します。

2. `dfs(i, cur, total)`: この内部関数は、深さ優先探索（DFS）を行います。
   - `i`: `candidates`の現在のインデックス
   - `cur`: 現在考慮している組み合わせ
   - `total`: `cur`の合計

3. `if total == target:`: `total`が`target`と一致する場合、現在の組み合わせを`res`に追加します。

4. `if i >= len(candidates) or total > target:`: インデックスが`candidates`の長さを超える、または`total`が`target`を超える場合、再帰の探索を終了します。

5. `cur.append(candidates[i])`: 現在の数値を組み合わせに追加します。

6. `dfs(i, cur, total + candidates[i])`: 現在の数値を含めて探索を続けます（同じ数値は複数回選択可能なため、インデックス`i`は変更されません）。

7. `cur.pop()`: 最後に追加した数値を取り除き、次の探索の準備をします。

8. `dfs(i + 1, cur, total)`: 現在の数値をスキップして、次の数値に移動して探索を続けます。

9. `dfs(0, [], 0)`: `dfs`関数を最初のインデックスから開始します。

10. `return res`: 探索が完了した後、結果のリスト`res`を返します。

この関数は、再帰的にすべての組み合わせを探索して`target`と一致するものを見つけます。
"""