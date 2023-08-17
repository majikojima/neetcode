from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS = len(matrix)
    COLS = len(matrix[0])

    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False
    
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True

    return False
    

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 1
print(searchMatrix(matrix, target))

"""
このコードは、m×nの行列において、ターゲットとなる値が存在するかどうかを確認するためのものです。行列は以下のような特性を持っています。

1. 各行は昇順にソートされています。
2. 各行の最初の整数は前の行の最後の整数よりも大きいです。

コードの大まかな流れは以下の通りです：

1. まず、ターゲットが存在する可能性がある行を見つけるために、バイナリサーチを使用します。
2. その行の中で再度バイナリサーチを使用して、ターゲットが存在するかどうかを確認します。

部分ごとの説明:

- `ROWS, COLS = len(matrix), len(matrix[0])`: 行列の行数と列数をそれぞれ`ROWS`と`COLS`に格納しています。

- 以下のwhileループで行を特定します:
  ```python
  top, bot = 0, ROWS - 1
  while top <= bot:
      row = (top + bot) // 2
      if target > matrix[row][-1]:
          top = row + 1
      elif target < matrix[row][0]:
          bot = row - 1
      else:
          break
  ```
  この部分は、バイナリサーチを用いてターゲットの値が存在する行を探しています。もしターゲットが現在の行の最大値よりも大きければ、次の行を探索します。逆に、ターゲットが現在の行の最小値よりも小さければ、前の行を探索します。

- `if not (top <= bot): return False`: ターゲットの値が存在する行が見つからなかった場合、`False`を返します。

- 以下のwhileループで特定の行内でターゲットの値を探索します:
  ```python
  row = (top + bot) // 2
  l, r = 0, COLS - 1
  while l <= r:
      m = (l + r) // 2
      if target > matrix[row][m]:
          l = m + 1
      elif target < matrix[row][m]:
          r = m - 1
      else:
          return True
  ```
  この部分では、再度バイナリサーチを用いて特定の行の中でターゲットの値が存在するかどうかを確認します。存在すれば`True`を返し、存在しなければ最後に`False`を返します。
"""