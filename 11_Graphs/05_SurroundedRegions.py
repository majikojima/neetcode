from typing import List

def solve(board: List[List[str]]) -> None:
    ROWS, COLS = len(board), len(board[0])

    def capture(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
            return
        board[r][c] = "T"
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)

    # 1. (DFS) Capture unsurrounded regions (O -> T)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                capture(r, c)

    # 2. Capture surrounded regions (O -> X)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"

    # 3. Uncapture unsurrounded regions (T -> O)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "T":
                board[r][c] = "O"

board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]
solve(board)
print(board)

"""
このコードは、与えられた2次元ボード上で囲まれている領域を特定して変更する目的で書かれています。特に、ボード上の`'O'`が境界に接している場合、それは囲まれていないとみなされ、囲まれている`'O'`は`'X'`に変更されます。

詳しく説明します。

### 全体の説明:
このコードは、2次元のボード（リストのリスト）を引数として受け取り、ボード上の囲まれていない領域を特定し、囲まれている`'O'`を`'X'`に変更します。

### 部分毎の説明:

1. **定数の定義**:
   ```python
   ROWS, COLS = len(board), len(board[0])
   ```
   ボードの行数と列数を取得して、`ROWS`と`COLS`という定数に保存します。

2. **capture関数**:
   ```python
   def capture(r, c):
       ...
   ```
   再帰的に動作するDFS（深さ優先探索）関数で、ボード上の特定の位置の`'O'`を`'T'`に変更します。これは、ボードの境界に接している`'O'`と、それに接続しているすべての`'O'`を特定するために使用されます。

3. **境界の`'O'`の特定**:
   ```python
   for r in range(ROWS):
       for c in range(COLS):
           if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
               capture(r, c)
   ```
   ボードの境界に位置する`'O'`を特定し、その`'O'`とそれに接続しているすべての`'O'`を`'T'`に変更します。

4. **囲まれている`'O'`の特定**:
   ```python
   for r in range(ROWS):
       for c in range(COLS):
           if board[r][c] == "O":
               board[r][c] = "X"
   ```
   ボード上でまだ`'O'`として残っている場所は、囲まれているとみなされます。そのため、これらの位置の`'O'`を`'X'`に変更します。

5. **`'T'`を`'O'`に戻す**:
   ```python
   for r in range(ROWS):
       for c in range(COLS):
           if board[r][c] == "T":
               board[r][c] = "O"
   ```
   最初のステップで`'T'`に変更された値を、もとの`'O'`に戻します。

最終的に、このコードは与えられたボードを変更し、囲まれている`'O'`を`'X'`に変更します。
"""

"""
もちろん、このコードの部分について詳しく解説します。

```python
# 1. (DFS) Capture unsurrounded regions (O -> T)
for r in range(ROWS):
    for c in range(COLS):
        if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
            capture(r, c)
```

この部分は、2次元のボード（board）のすべてのセルを調べるためのネストされた2つのforループを使用しています。このネストされたループを通じて、各セルが以下の条件を満たすかどうかをチェックしています。

1. セルの内容が "O" である。
2. セルがボードの境界、つまり最上部、最下部、最左端、または最右端に位置している。

この条件を満たすセルは、`capture`関数を使って"O"から"T"に変更されます。この変更は、後のステップで「囲まれていない」セルと「囲まれている」セルを区別するために行われます。

なぜこのような操作を行うのかというと、境界に接している"O"は、ボードの外側からアクセスできるため、囲まれていないとみなされます。このような"O"は、後のステップで変更されることなくそのまま残す必要があります。したがって、このステップでは、これらの囲まれていない"O"を一時的に"T"に変更して、後のステップで区別しやすくしています。

具体的には、`capture`関数は深さ優先探索（DFS）を使用して、指定されたセルから出発し、そのセルと連結しているすべての"O"を探索して"T"に変更します。これにより、境界に接している"O"とその隣接するすべての"O"が"T"に変更されることになります。
"""