from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    # O(1)
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False

    # determine which rows/cols need to be zero
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
print(matrix)

"""
この関数 `setZeroes` は、与えられた2次元の行列 (`matrix`) において、0が存在する行や列を探して、その行や列の全ての要素を0に変更するものです。

**大まかな説明**:
関数は次の手順で動作します：
1. まず、どの行や列に0が存在するかを判断します。
2. それを記録するために、その行の最初の要素とその列の最初の要素を0に設定します。
3. 最後に、これらのマーカーを使用して、該当する行や列の全ての要素を0に設定します。

**部分毎の説明**:

1. 初期設定:
    - `ROWS, COLS = len(matrix), len(matrix[0])`: 行と列の数を取得します。
    - `rowZero = False`: これは最初の行に0があるかどうかを追跡するための変数です。

2. 0が存在する行や列を特定します。
    ```python
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True
    ```
    ここでは、0の要素を見つけると、その要素が所属する行と列の最初の要素を0に設定します。

3. マーカーを使用して0を設定します。
    ```python
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    ```

4. 最初の列に0を設定します（必要な場合）。
    ```python
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0
    ```

5. 最初の行に0を設定します（必要な場合）。
    ```python
    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0
    ```

このアプローチの利点は、追加のメモリを使用せずに、行列自体を変更して問題を解決することができる点にあります。
"""