def uniquePaths(m: int, n: int) -> int:
    row = [1] * n

    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1):
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow
    return row[0]

    # O(n * m) O(n)

m = 3
n = 7
print(uniquePaths(m, n))

m = 3
n = 2
print(uniquePaths(m, n))

"""
このコードは、`m x n` のグリッドの左上から右下までのユニークなパスの数を求めるためのものです。移動は右または下だけできます。この問題は、動的計画法を使用して解くのが一般的です。

コードの部分ごとの説明を行います：

1. **初期化**:
    ```python
    row = [1] * n
    ```
   この行は、現在の行のすべてのセルを`1`で初期化します。最初の行と最初の列の各セルへのユニークなパスの数は1だけです（1通りの方法しかないため）。そのため、最初の行の初期化はこのように行われます。

2. **動的計画法のループ**:
    ```python
    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1):
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow
    ```
    - 外側のループは、2行目から最後の行までを繰り返します。
    - `newRow`は次の行を計算するための一時的なリストで、全てのセルを`1`で初期化します。
    - 内側のループでは、右端から左に向かって各セルの値を計算します。各セルの値は、そのセルの右隣のセルとそのセルの下のセルの合計です。ここでは`newRow[j + 1]`が右隣のセル、`row[j]`が下のセルを示しています。
    - ループが終了すると、`newRow`は次の行の値が計算され、`row`に割り当てられるため、次の反復ではこの行が「現在の行」として使用されます。

3. **結果の返却**:
    ```python
    return row[0]
    ```
   最後に、左上隅から右下隅までのユニークなパスの数（最後の行の最初のセルの値）を返します。

4. **計算量のコメント**:
    ```python
    # O(n * m) O(n)
    ```
   このコメントは、このアルゴリズムの時間計算量が`O(n * m)`で、空間計算量が`O(n)`であることを示しています。ここで`n`は列の数、`m`は行の数です。
"""