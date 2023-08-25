from typing import List

def numIslands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    row = len(grid)
    col = len(grid[0])
    visit = set()
    island = 0

    def dfs(r, c):
        if (
            r not in range(row)
            or c not in range(col)
            or grid[r][c] == "0"
            or (r, c) in visit
        ):
            return
        
        visit.add((r, c))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dr, dc in directions:
            dfs(r + dr, c + dc)
        return
    
    for r in range(row):
        for c in range(col):
            if grid[r][c] == "1" and (r, c) not in visit:
                island += 1
                dfs(r, c)
    
    return island

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))

"""
このアルゴリズムは、与えられた2次元グリッド内の島の数をカウントするものです。ここでの「島」とは、連続する1の塊を指します。0は水を、1は土地を表します。2つの1が水平または垂直に隣接している場合、それらは連続していると見なされます。

アルゴリズムの大まかな説明:
1. グリッドの各セルを調査して、未訪問で1のセルを見つける。
2. そのようなセルを見つけたら、深さ優先探索(DFS)を使用して、そのセルから接続されているすべての1のセルを訪問します。
3. このプロセスが終了すると、島の数を1つ増やします。
4. グリッド内のすべてのセルを調査し終えると、島の合計数を返します。

部分ごとの説明:

1. **初期条件の確認**:
   ```python
   if not grid or not grid[0]:
       return 0
   ```
   グリッドが空の場合、島は0として返されます。

2. **変数の初期化**:
   ```python
   islands = 0
   visit = set()
   rows, cols = len(grid), len(grid[0])
   ```
   - `islands`: 島の数をカウントするための変数。
   - `visit`: 既に訪問したセルを追跡するための集合。
   - `rows` と `cols`: グリッドの行数と列数。

3. **深さ優先探索 (DFS) の定義**:
   ```python
   def dfs(r, c):
       ...
   ```
   この関数は、指定されたセルから接続されたすべての1のセルを訪問します。セルがグリッドの境界外である、または0である、またはすでに訪問されている場合、探索はそこで終了します。

4. **主要な探索ループ**:
   ```python
   for r in range(rows):
       for c in range(cols):
           if grid[r][c] == "1" and (r, c) not in visit:
               islands += 1
               dfs(r, c)
   ```
   すべてのセルを調査し、未訪問で1のセルを見つけるたびに、島の数を1つ増やし、DFSを使ってその島のすべての部分を訪問します。

5. **結果の返却**:
   ```python
   return islands
   ```
   最終的に、見つけた島の合計数を返します。
"""

"""
もちろん、この関数の中身について詳しく説明します。

`dfs`は深さ優先探索 (DFS) を行うための関数です。この関数は与えられたグリッド内の特定のセル `(r, c)` を開始点として、それと接続されているすべての「1」のセルを訪問します。

1. **終了条件**:
   ```python
   if (
       r not in range(rows)
       or c not in range(cols)
       or grid[r][c] == "0"
       or (r, c) in visit
   ):
       return
   ```
   上記の条件は以下のいずれかが満たされるときに再帰的な探索を終了します:
   - `r not in range(rows)`: 現在のセルがグリッドの行の範囲外である。
   - `c not in range(cols)`: 現在のセルがグリッドの列の範囲外である。
   - `grid[r][c] == "0"`: 現在のセルが「0」であり、したがって訪問する必要がない。
   - `(r, c) in visit`: このセルは既に訪問されている。

2. **訪問のマーク**:
   ```python
   visit.add((r, c))
   ```
   現在のセル `(r, c)` を訪問したとマークします。これにより、同じセルを再び訪問することを避けることができます。

3. **隣接セルの探索方向**:
   ```python
   directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
   ```
   `directions`は現在のセルの上下左右の隣接セルへの移動方向を示しています。これにより、すべての隣接セルを効果的に調査できます。

4. **隣接セルの探索**:
   ```python
   for dr, dc in directions:
       dfs(r + dr, c + dc)
   ```
   現在のセル `(r, c)` からの各方向について、隣接するセルを再帰的に探索します。これにより、連続した「1」のセルを深さ優先で訪問することができます。

この`dfs`関数のおかげで、連続した「1」の塊、つまり島を効果的に探索することができます。
"""