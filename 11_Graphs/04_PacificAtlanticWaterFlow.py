from typing import List

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visit, prevHeight):
        if (
            (r, c) in visit
            or r < 0
            or c < 0
            or r == ROWS
            or c == COLS
            or heights[r][c] < prevHeight
        ):
            return
        visit.add((r, c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])

    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])
    return res

heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
print(pacificAtlantic(heights))

heights = [[1]]
print(pacificAtlantic(heights))

"""
このコードは、与えられた`heights`マトリックス上で、太平洋と大西洋の両方に水が流れるセルを探し出すものです。以下に、コードの大まかな説明と部分ごとの説明を示します。

**大まかな説明**:
- 太平洋（`pac`）および大西洋（`atl`）への流れを追跡するための2つの集合を作成します。
- 両方の海からのDFS (深さ優先探索)を使用して、どのセルから水がどの海に流れるかを追跡します。
- 最後に、太平洋と大西洋の両方に流れるセルのリストを返します。

**部分毎の説明**:

1. **初期化**:
    ```python
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()
    ```
    - グリッドの行数と列数を取得します。
    - 太平洋(`pac`)と大西洋(`atl`)に流れるセルを追跡するための2つの集合を初期化します。

2. **DFS関数の定義**:
    ```python
    def dfs(r, c, visit, prevHeight):
        ...
    ```
    - 指定されたセルから開始して、深さ優先探索(DFS)を使用して隣接セルに移動します。
    - 既に訪問したセルや、前のセルよりも低い高さのセルへは移動しません。
    - この関数は再帰的に自分自身を呼び出して、グリッド内のセルを探索します。

3. **海岸線からのDFSの開始**:
    ```python
    for c in range(COLS):
        ...
    for r in range(ROWS):
        ...
    ```
    - 太平洋は上と左の境界から、大西洋は下と右の境界からDFSを開始します。
    - これにより、それぞれの海への流れるセルを`pac`および`atl`に追加します。

4. **結果の計算**:
    ```python
    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])
    return res
    ```
    - グリッド内の各セルを反復処理し、そのセルが太平洋(`pac`)と大西洋(`atl`)の両方の集合に存在する場合、そのセルの座標を結果リストに追加します。
    - 最後に、太平洋と大西洋の両方に流れるセルのリストを返します。
"""