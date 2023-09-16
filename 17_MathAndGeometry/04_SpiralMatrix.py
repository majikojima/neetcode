from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # get every i in the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        # get every i in the right col
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1
        if not (left < right and top < bottom):
            break
        # get every i in the bottom row
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1
        # get every i in the left col
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))

"""
この関数 `spiralOrder` は、与えられた2次元行列 (matrix) の要素を螺旋状に読み取り、それらの要素を1次元のリストとして返します。

**大まかな説明**:
`spiralOrder` 関数は、行列の外周から内側に向かって、上の行、右の列、下の行、左の列の順に要素を読み取り、それを結果のリスト `res` に追加していきます。この操作を行列の全ての要素を読み取るまで繰り返します。

**部分毎の説明**:

1. `res = []`: 結果を格納する空のリストを初期化します。
2. 初期値設定: 
    - `left, right`: 行列の左端と右端を示すインデックスです。
    - `top, bottom`: 行列の上端と下端を示すインデックスです。
3. `while left < right and top < bottom`: このループは、まだ読み取る要素が存在する限り続きます。
4. 上の行の要素を読み取り:
    ```python
    for i in range(left, right):
        res.append(matrix[top][i])
    top += 1
    ```
5. 右の列の要素を読み取り:
    ```python
    for i in range(top, bottom):
        res.append(matrix[i][right - 1])
    right -= 1
    ```
6. 以下の条件 `if not (left < right and top < bottom):` は、行や列の要素を読み取った後に、まだ読み取る要素が残っているかどうかをチェックします。もし残っていなければ、ループを終了します。
7. 下の行の要素を読み取り:
    ```python
    for i in range(right - 1, left - 1, -1):
        res.append(matrix[bottom - 1][i])
    bottom -= 1
    ```
8. 左の列の要素を読み取り:
    ```python
    for i in range(bottom - 1, top - 1, -1):
        res.append(matrix[i][left])
    left += 1
    ```
9. `return res`: 最後に、結果のリスト `res` を返します。

この関数は、行列の外周から開始して、中央に向かって螺旋状に要素を読み取り、それを結果のリストに追加していきます。
"""