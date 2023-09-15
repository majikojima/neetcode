from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # save the topleft
            topLeft = matrix[top][l + i]

            # move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # move top left into top right
            matrix[top + i][r] = topLeft
        r -= 1
        l += 1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)
print(matrix)

"""
このコードは、与えられた2次元リスト（行列）を90度回転させる関数です。この操作はインプレースで行われ、新しい行列を作成することなく元の行列を変更します。

コードの詳細に入る前に、全体の流れを説明します。

### 大まかな説明:
この関数は、与えられた2次元の行列を時計回りに90度回転させる役目を果たします。この処理は、外側のレイヤーから内側のレイヤーへと進んでいきます。それぞれのレイヤーで、4つの辺の要素が交換されていくことで、回転が実現されます。

### 部分毎の説明:
1. **初期化**:
    ```python
    l, r = 0, len(matrix) - 1
    ```
    `l` と `r` は、現在処理しているレイヤーの左上と右下のインデックスを示しています。

2. **レイヤーの処理**:
    ```python
    while l < r:
    ```
    このループは外側のレイヤーから順に内側へと進んでいきます。

3. **各レイヤーの要素の交換**:
    ```python
    for i in range(r - l):
    ```
    このループは、現在のレイヤーにおける要素の交換を行っています。

4. **四隅の要素の交換**:
    以下の4つの操作は、行列の四隅の要素を回転させるためのものです。
    - 左上を保存
    - 左下を左上に移動
    - 右下を左下に移動
    - 右上を右下に移動
    - 保存していた左上を右上に移動

5. **次のレイヤーへ移動**:
    ```python
    r -= 1
    l += 1
    ```
    上記の操作で、外側のレイヤーの要素の回転が完了すると、次の内側のレイヤーに移るために `l` と `r` を更新しています。

このアルゴリズムは、行列の各レイヤーを独立して回転させることで、全体を90度回転させる効果を持ちます。
"""