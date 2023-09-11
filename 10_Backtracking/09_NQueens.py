from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)

    res = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res

n = 4
print(solveNQueens(n))

"""
このコードは、N-Queens問題を解くためのものです。N-Queens問題とは、n x n のチェスボードにn個のクイーンを配置する問題で、どの2つのクイーンも互いに攻撃しないように配置しなければならないというものです。

**大まかな説明**:
- n x n のチェスボードに、任意の2つのクイーンが互いに攻撃しないようにn個のクイーンを配置する全ての可能な解を見つけます。
- バックトラッキングを使用して、各行に1つのクイーンを配置します。クイーンが置かれると、その列、両方の対角線は次のクイーンの配置の選択肢から除外されます。

**部分毎の説明**:

1. **変数の初期化**:
   - `col`, `posDiag`, `negDiag`: これらのセットは、クイーンが配置されている列や対角線を追跡します。
   - `res`: 有効なボードの配置を保存するリストです。
   - `board`: n x n のチェスボードを表す2次元リスト。初期状態では、すべてのセルには"."が配置されています。

2. **`backtrack`関数**:
   - 再帰的なバックトラッキング関数で、クイーンの位置を試みます。
   - `r`は現在の行を表す。
   - もし`r`がnに等しい場合、ボードにはn個のクイーンが配置されているので、その配置を`res`に追加します。
   - 各列`c`について、その列や対角線にクイーンが存在しない場合、新しいクイーンを配置します。
   - クイーンを配置した後、再帰的に次の行に進みます。
   - 再帰呼び出しから戻った後、クイーンの位置を取り消して、次の列での配置を試みます。

3. **関数の実行**:
   - `backtrack(0)`: バックトラッキングを開始します。最初は0行目から始めます。

最終的に、`res`にはn x nのボードの有効な全ての配置が保存され、それがこの関数の戻り値となります。
"""

"""
この`backtrack`関数はN-Queens問題のバックトラッキング解法の核心部分です。この関数は再帰的にクイーンをチェスボードの各行に配置しようと試みます。

以下、関数の各部分の説明です。

1. **基本ケース**:
   ```python
   if r == n:
       copy = ["".join(row) for row in board]
       res.append(copy)
       return
   ```
   - `if r == n:`: これは全ての行にクイーンが配置されたことを意味します。
   - `copy`: 現在のボードの状態のコピーを作成します。各行は文字列として保存されます。
   - `res.append(copy)`: このコピーを解のリスト`res`に追加します。

2. **各列に対するループ**:
   ```python
   for c in range(n):
   ```
   - 現在の行`r`の各列`c`にクイーンを配置することを試みます。

3. **クイーンの配置の検証**:
   ```python
   if c in col or (r + c) in posDiag or (r - c) in negDiag:
       continue
   ```
   - もし列`c`や対角線にすでにクイーンが配置されているなら、現在の列は無視されます。

4. **クイーンの配置**:
   ```python
   col.add(c)
   posDiag.add(r + c)
   negDiag.add(r - c)
   board[r][c] = "Q"
   ```
   - クイーンを現在のセルに配置します。
   - 使用済みの列や対角線を追跡するためのセットを更新します。

5. **再帰的な呼び出し**:
   ```python
   backtrack(r + 1)
   ```
   - 次の行に進んで、クイーンの配置を試みます。

6. **バックトラック（状態のリセット）**:
   ```python
   col.remove(c)
   posDiag.remove(r + c)
   negDiag.remove(r - c)
   board[r][c] = "."
   ```
   - 現在のクイーンの配置を取り消します。これにより、次の列でのクイーンの配置を試みる準備ができます。

この`backtrack`関数は再帰的に次の行を試しながら、全ての列と対角線に対してクイーンが配置できるかどうかを検証します。全ての行が試された後で、解のリスト`res`に有効な配置が追加されます。
"""