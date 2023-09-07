from collections import Counter, defaultdict
from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if(
            r < 0
            or c < 0
            or r >= ROWS
            or c >= COLS
            or word[i] != board[r][c]
            or (r, c) in path
        ):
            return False
        
        path.add((r, c))
        res = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i+ 1)
            or dfs(r, c + 1, i+ 1)
            or dfs(r, c - 1, i+ 1)
        )
        path.remove((r,c))
        return res
        
    count = defaultdict(int, sum(map(Counter, board), Counter()))
    if count[word[0]] > count[word[1]]:
        word = word[::-1]
    
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))

word = "SEE"
print(exist(board, word))

word = "ABCB"
print(exist(board, word))

"""
このコードは、与えられた2次元の文字盤(`board`)上で、指定された文字列(`word`)が存在するかどうかを探すためのものです。具体的には、`board`上のどこかの位置から始まり、上下左右のいずれかの隣接セルに移動することで、文字列`word`を形成できるかどうかをチェックします。

### 大まかな説明:
- `board`上の全てのセルを開始点としてDFS(深さ優先探索)を行い、`word`が形成できるかをチェックします。
- `path`というsetを使って、既に探索済みのセルを管理します。
- `word`の最初と最後の文字の出現頻度をチェックし、もし最初の文字の出現頻度が最後の文字よりも多い場合、`word`を逆順にして最適化します。
- 探索が成功するとTrueを、失敗するとFalseを返します。

### 部分毎の説明:

1. `ROWS, COLS = len(board), len(board[0])`  
    - 2次元の`board`の行数と列数を取得します。

2. `path = set()`  
    - 探索済みのセルを保存するためのsetを初期化します。

3. `dfs(r, c, i)`  
    - rとcは現在のセルの行と列を表し、iは現在探索中の`word`のインデックスを示します。
    - この再帰関数は深さ優先探索(DFS)を使用して`board`上を探索します。

4. `if i == len(word):`  
    - 全ての文字がマッチした場合、Trueを返します。

5. 以下のif文は、探索が失敗する条件をチェックします:  
    - 現在のセルが`board`の範囲外であるか
    - 現在のセルの文字が探索中の`word`の文字と一致しないか
    - 現在のセルが既に探索済みであるか

6. `path.add((r, c))`と`path.remove((r, c))`  
    - 現在のセルを探索済みとして追加、または削除します。

7. `dfs(r + 1, c, i + 1)`や`dfs(r, c + 1, i + 1)`など  
    - 現在のセルの上下左右のセルを探索します。

8. `count = defaultdict(int, sum(map(Counter, board), Counter()))`  
    - `board`上の各文字の出現頻度を計算します。

9. `if count[word[0]] > count[word[-1]]:`  
    - `word`の最初と最後の文字の出現頻度を比較し、最初の文字の方が多ければ`word`を逆順にします。

10. 最後の二重ループ  
    - `board`の全てのセルを開始点としてDFSを実行し、探索が成功するかどうかをチェックします。

全体の計算量は`O(n * m * 4^n)`で、`n`は`board`の行数、`m`は列数を示しています。
"""

"""
1. `if count[word[0]] > count[word[-1]]:`に関して:

この最適化は、探索開始点の候補数を減らすために導入されています。`board`上で`word`の最初の文字が多く存在する場合、そのすべての位置から探索を開始します。しかし、`word`の最後の文字が`board`上でより少なく存在する場合、その文字から探索を開始することで、全体としての探索のスタートポイントの数を減少させることができます。そうすることで、全体の探索時間を短縮することが期待されます。

2. `count = defaultdict(int, sum(map(Counter, board), Counter()))`に関して:

このコードは`board`上の各文字の出現回数を計算しています。少し複雑に見えるかもしれませんが、以下のようにシンプルな形に書き換えることができます。

```python
from collections import Counter

count = Counter()
for row in board:
    count.update(row)
```

この書き換えられたコードも、`board`上の各文字の出現頻度を`count`辞書に保存します。
"""

"""
「SEE」という単語をboard上で探す場合のシミュレーションを以下に示します。上記の`exist`関数の動作を元に説明します。

まず、探索の最適化の部分：
```python
count = defaultdict(int, sum(map(Counter, board), Counter()))
if count[word[0]] > count[word[-1]]:
    word = word[::-1]
```
board内の各文字の出現頻度を計算すると：
- A: 2
- B: 1
- C: 2
- E: 3
- S: 2
- F: 1
- D: 1

wordの最初の文字"S"と最後の文字"E"の出現頻度を比較すると、"E"の方が"S"よりも多いため、wordを逆順にする処理は行われません。

次に、boardの各セルを探索開始点としてDFSを使用して探索を行います：

1. 最初のセル"A"から開始。"SEE"とマッチしないため、次のセルへ。
2. セル"B"、"SEE"とマッチしないため、次のセルへ。
3. セル"C"、"SEE"とマッチしないため、次のセルへ。
4. セル"E"、"SEE"の最初の文字とマッチ。
   - 右の"S"に移動（"SEE"の2文字目とマッチ）
     - 右の"S"に移動（しかし"S"は"SEE"の3文字目とマッチしないため、探索を戻す）
     - 下の"D"に移動（"SEE"とマッチしないため、探索を戻す）
   - 下の"S"に移動（"SEE"の2文字目とマッチ）
     - 右の"C"に移動（しかし"C"は"SEE"の3文字目とマッチしないため、探索を戻す）
     - 下の"A"に移動（"SEE"とマッチしないため、探索を戻す）
5. セル"S"、"SEE"とマッチしないため、次のセルへ。
6. セル"F"、"SEE"とマッチしないため、次のセルへ。
7. セル"C"、"SEE"とマッチしないため、次のセルへ。
8. セル"S"、"SEE"の最初の文字とマッチ。
   - 右の"E"に移動（"SEE"の2文字目とマッチ）
     - 右の"E"に移動（"SEE"の3文字目とマッチ、完全なマッチが見つかったので探索を終了）

したがって、"SEE"という単語はboard上で存在すると確認できます。
"""