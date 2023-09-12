from typing import List

def longestIncreasingPath(matrix: List[List[int]]) -> int:
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = {}  # (r, c) -> LIP

    def dfs(r, c, prevVal):
        if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
            return 0
        if (r, c) in dp:
            return dp[(r, c)]

        res = 1
        res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
        res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
        dp[(r, c)] = res
        return res

    for r in range(ROWS):
        for c in range(COLS):
            dfs(r, c, -1)
    return max(dp.values())

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))

matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix))

matrix = [[1]]
print(longestIncreasingPath(matrix))

"""
このコードは、与えられた2次元のマトリックス内で最も長い増加するパス（LIP: Longest Increasing Path）を探す問題を解決します。この増加するパスとは、隣接するセルを含む連続した数の増加するシーケンスを指します。隣接するセルとは、上下左右に隣接するセルを意味します。

以下は、各部分の説明です。

1. **変数の初期化**:
   - `ROWS, COLS`: マトリックスの行数と列数。
   - `dp`: この辞書は各セル `(r, c)` から始まる最も長い増加するパスの長さを保存します。

2. **dfs関数**:
   - `dfs(r, c, prevVal)`: 再帰的な深さ優先探索を実行して、位置 `(r, c)` から始まる最も長い増加するパスの長さを返します。
   - この関数は次の条件で終了します：
     1. 現在の位置がマトリックスの境界を超えているか、
     2. 現在のセルの値が前のセルの値以下である場合。
   - 4つの方向（上、下、左、右）それぞれに対して、次のセルが増加するパスの一部としてカウントされるかどうかを確認します。
   - 最後に、`dp`辞書に結果をキャッシュします。

3. **全セルの探索**:
   - この2重ループは、マトリックス内のすべてのセルについて`dfs`を呼び出します。
   - `dfs(r, c, -1)`: ここで、`-1`は現在のセルの値が前のセルの値より大きいと確認するためのダミーの前のセルの値として使用されます。

4. **結果の返却**:
   - `return max(dp.values())`: `dp`辞書のすべての値の中で最も大きいもの（最も長い増加するパス）を返します。

このコードは深さ優先探索（DFS）を使用してマトリックス内のすべてのセルからの最も長い増加するパスを計算し、メモ化を使って計算時間を短縮します。
"""