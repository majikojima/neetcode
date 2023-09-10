from typing import List
import collections

def orangesRotting(grid: List[List[int]]) -> int:
    q = collections.deque()
    fresh = 0
    time = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append((r, c))

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while fresh > 0 and q:
        length = len(q)
        for i in range(length):
            r, c = q.popleft()

            for dr, dc in directions:
                row, col = r + dr, c + dc
                # if in bounds and nonrotten, make rotten
                # and add to q
                if (
                    row in range(len(grid))
                    and col in range(len(grid[0]))
                    and grid[row][col] == 1
                ):
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
        time += 1
    return time if fresh == 0 else -1

grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
print(orangesRotting(grid))

grid = [[0,2]]
print(orangesRotting(grid))

"""
このコードは、与えられた`grid`マトリックス上の腐ったオレンジがどれだけの時間で新鮮なオレンジを腐らせるかを計算するものです。以下に、コードの大まかな説明と部分ごとの説明を示します。

**大まかな説明**:
- このコードは、グリッド上の新鮮なオレンジ（値が1）と腐ったオレンジ（値が2）を探します。
- 腐ったオレンジからBFS (幅優先探索) を開始して、新鮮なオレンジを腐らせます。
- 全てのオレンジが腐ったかどうかを確認し、全て腐った場合は必要な時間を、そうでなければ-1を返します。

**部分毎の説明**:

1. **初期化**:
    ```python
    q = collections.deque()
    fresh = 0
    time = 0
    ```
    - `q`は腐ったオレンジの位置を保持するためのキューです。
    - `fresh`は新鮮なオレンジの数をカウントするための変数です。
    - `time`はオレンジが完全に腐るのにかかる時間をカウントするための変数です。

2. **新鮮なオレンジと腐ったオレンジの探索**:
    ```python
    for r in range(len(grid)):
        ...
    ```
    - このループでは、新鮮なオレンジをカウントし、腐ったオレンジの位置をキューに追加します。

3. **隣接セルへの移動のための方向ベクトルの初期化**:
    ```python
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    ```
    - これは、現在のセルから北、南、東、西の隣接セルに移動するための方向ベクトルです。

4. **BFSの開始**:
    ```python
    while fresh > 0 and q:
        ...
    ```
    - このループでは、まだ新鮮なオレンジが存在し、キューに腐ったオレンジが存在する限り、BFSを使用して新鮮なオレンジを腐らせます。

5. **結果の計算**:
    ```python
    return time if fresh == 0 else -1
    ```
    - 全てのオレンジが腐った場合（`fresh == 0`）、必要な時間を返します。
    - そうでない場合は、-1を返します。これは、全てのオレンジが腐ることができないことを意味します。
"""