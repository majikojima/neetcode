from typing import List
import heapq

def swimInWater(grid: List[List[int]]) -> int:
    N = len(grid)
    visit = set()
    minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    visit.add((0, 0))
    while minH:
        t, r, c = heapq.heappop(minH)
        if r == N - 1 and c == N - 1:
            return t
        for dr, dc in directions:
            neiR, neiC = r + dr, c + dc
            if (
                neiR < 0
                or neiC < 0
                or neiR == N
                or neiC == N
                or (neiR, neiC) in visit
            ):
                continue
            visit.add((neiR, neiC))
            heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

grid = [
    [0,2],
    [1,3]
]
print(swimInWater(grid))

grid = [
    [0,1,2,3,4],
    [24,23,22,21,5],
    [12,13,14,15,16],
    [11,17,18,19,20],
    [10,9,8,7,6]
]
print(swimInWater(grid))

"""
このコードは、与えられた2次元の`grid`での水泳をシミュレートします。各セルの値は、そのセルに到達するための最短の時間（または最大の高さ）を示しています。この問題の目的は、左上のコーナーから右下のコーナーへ移動するのに必要な最短の時間を求めることです。

**大まかな説明**:
コードは、最小ヒープを使ってシミュレートされた水泳を行い、最短の時間を返します。ヒープには、時間（または最大の高さ）、行、列の情報が含まれています。各ステップで、ヒープから最短の時間のセルを取り出し、そのセルから到達可能なすべての隣接セルをヒープに追加します。

**部分毎の説明**:

1. `N = len(grid)`:
    - グリッドのサイズを取得します。

2. `visit = set()`:
    - すでに訪れたセルを追跡するための集合です。

3. `minH = [[grid[0][0], 0, 0]]`:
    - 初期の最小ヒープ。開始地点は左上のコーナーです。

4. `directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]`:
    - セルの4つの隣接セルへの移動方向です。

5. `while minH`:
    - ヒープに要素がある限り続けます。

6. `t, r, c = heapq.heappop(minH)`:
    - ヒープから最短の時間のセルの情報を取得します。

7. `if r == N - 1 and c == N - 1`:
    - もし目的地（右下のコーナー）に達した場合、現在の時間を返します。

8. `for dr, dc in directions`:
    - 4つの隣接セルの方向に対してループを行います。

9. `neiR, neiC = r + dr, c + dc`:
    - 現在のセルからの隣接セルの位置を計算します。

10. `if neiR < 0 or ...`:
    - グリッドの外に出る、またはすでに訪れたセルに移動する場合、この方向をスキップします。

11. `visit.add((neiR, neiC))`:
    - 隣接セルを訪問済みの集合に追加します。

12. `heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])`:
    - 隣接セルの情報と、そのセルへの移動にかかる時間をヒープに追加します。時間は、現在のセルの時間と隣接セルの値の大きい方です。
"""