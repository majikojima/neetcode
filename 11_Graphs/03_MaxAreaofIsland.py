from typing import List

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = set()

    def dfs(r, c):
        if(
            r < 0
            or c < 0
            or r >= ROWS
            or c >= COLS
            or grid[r][c] == 0
            or (r, c) in visited
        ):
            return 0
        visited.add((r, c))
        return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

    area = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1 and (r, c) not in visited:
                area = max(area, dfs(r, c))
    return area

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(maxAreaOfIsland(grid))

grid = [
    [0,0,0,0,0,0,0,0]
]
print(maxAreaOfIsland(grid))

"""
このコードは、与えられた二次元グリッド上の島（1として表される連続したセルの領域）の最大の面積を計算するものです。

### 大まかな説明：
グリッドを走査し、まだ訪問されていないセルを発見する度に深さ優先探索（DFS）を使用してそのセルが属する島の面積を計算します。その島の面積が現在の最大面積よりも大きければ、最大面積を更新します。最後に、最大の島の面積を返します。

### 部分毎の説明：

1. `ROWS, COLS = len(grid), len(grid[0])`: グリッドの行数と列数を取得します。
2. `visited = set()`: 訪問済みのセルを追跡するための集合を初期化します。

3. `def dfs(r, c):`: セル`(r, c)`から開始して、島の面積を再帰的に計算する関数を定義します。
    - この関数内の条件分岐は、セルがグリッドの範囲外であるか、セルが水（0として表される）であるか、または既に訪問済みである場合、`0`を返します。
    - そうでなければ、現在のセルを訪問済みとしてマークし、隣接するセルに対して同じ関数を再帰的に呼び出し、結果を合計してその島の面積を計算します。

4. `area = 0`: 最大の島の面積を追跡するための変数を初期化します。

5. 外部の2重ループ(`for r in range(ROWS):`と`for c in range(COLS):`)は、グリッドの各セルを走査します。

6. `if grid[r][c] == 1 and (r, c) not in visited:`: まだ訪問されていない土地のセル（1として表される）を見つけた場合、
    - そのセルを起点としてDFSを使用して島の面積を計算します。
    - 計算された面積が現在の最大面積よりも大きい場合、最大面積を更新します。

7. `return area`: 最終的に、最大の島の面積を返します。
"""