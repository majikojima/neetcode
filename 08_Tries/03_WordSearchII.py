from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    for w in words:
        root.addWord(w)

    ROWS, COLS = len(board), len(board[0])
    res, visit = set(), set()

    def dfs(r, c, node, word):
        if(
            r not in range(ROWS)
            or c not in range(COLS)
            or board[r][c] not in node.children
            or node.children[board[r][c]].refs < 1
            or (r, c) in visit
        ):
            return
        
        visit.add((r, c))
        node = node.children[board[r][c]]
        word += board[r][c]
        if node.isWord:
            node.isWord = False
            res.add(word)
            root.removeWord(word)

        dfs(r + 1, c, node, word)
        dfs(r - 1, c, node, word)
        dfs(r, c + 1, node, word)
        dfs(r, c - 1, node, word)
        visit.remove((r, c))

    for r in range(ROWS):
        for c in range(COLS):
            dfs(r, c, root, "")

    return list(res)

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(findWords(board, words))

"""
このコードは、与えられた2次元のボード上で指定された単語リストに存在する単語を探索するものです。この探索のために、高速化技術としてTrie（プレフィックスツリー）を利用しています。

具体的に各部分を解説します。

### `TrieNode`クラス:
- Trie（プレフィックスツリー）のノードを表すクラス。
  - `children`: 現在の文字から次の文字へのマッピングを格納する辞書。
  - `isWord`: 現在のノードが単語の終端を示すかどうかのフラグ。
  - `refs`: このノードを参照する単語の数。 
  - `addWord`: 与えられた単語をTrieに追加するメソッド。
  - `removeWord`: 与えられた単語をTrieから削除するメソッド（具体的には参照カウントを減少させる）。

### `Solution`クラス:

- `findWords`:
  - 2次元のボードと単語リストを入力として受け取り、ボード上で見つかった単語のリストを返します。
  
  1. まず、与えられた単語すべてをTrieに追加します。
  2. ボード上のすべてのセルを探索し、そのセルから始まる可能性のある単語を深さ優先探索(DFS)で探します。
  3. DFSの過程で、ボードの境界を超えたり、既に訪れたセルを再び訪れることを避けるための条件がいくつか設定されています。
  4. 単語が見つかった場合、それを結果のセットに追加し、その単語をTrieから削除します（これにより、同じ単語が2回追加されることを防ぐことができます）。

このコードの主な利点は、Trieを使用することで高速な単語の検索とプレフィックスのマッチングが可能になることです。
"""

"""
了解しました。指定された`findWords`関数の詳細な説明を行います。

### 概要:
この関数は、与えられた`board`（2Dの文字配列）上で、`words`リストに含まれる単語を検索するためのものです。もし単語がボード上で見つかれば、その単語を結果リストに追加します。

### 手順:

1. **初期設定**:
    - Trieのルートノードを初期化します。
    - 各単語をTrieに追加します。
    - ボードの行と列の数を取得します。
    - `res`（結果を格納する集合）と`visit`（訪問したセルを記録する集合）を初期化します。

2. **DFS関数**:
    - DFS (深さ優先探索) を使用して、ボード上の各セルから単語を探索します。
    - 関数は以下のパラメータを持ちます：行のインデックス(`r`)、列のインデックス(`c`)、現在のTrieノード(`node`)、そして現在の単語(`word`)。
    - 以下の条件のいずれかが満たされる場合、DFSのこの特定の呼び出しは終了します：
        - 現在のセルがボードの外にある。
        - 現在のセルの文字がTrieノードの子供として存在しない。
        - 現在のセルの文字に対応するTrieノードの参照カウントが0以下。
        - 現在のセルが既に訪問されている。
    - 現在のセルを訪問したとしてマークします。
    - 現在のセルの文字を単語に追加します。
    - その文字がTrie内で単語の終わりを示している場合、単語を結果集合に追加し、Trieからその単語を削除します。
    - 現在のセルの上下左右の隣接セルでDFSを再帰的に呼び出します。
    - 現在のセルの訪問マークを解除します。

3. **ボード上の各セルに対してDFSを呼び出す**:
    - ボード上の各セルに対してDFSを呼び出し、単語の検索を開始します。

4. **結果を返す**:
    - `res`集合をリストに変換して返します。

この関数のポイントは、DFSを使用してボード上の各セルから単語を探索することです。そして、Trieデータ構造を使用して効率的に単語の存在を確認します。
"""

"""
はい、ご指摘の通りです。このアルゴリズムは実際にはかなり複雑な部分があります。主に以下の理由からです：

1. **Trieの使用**: Trieは、単語のプレフィックスを高速に検索するためのデータ構造です。ただし、その実装や利用にはいくつかの細かい点が含まれるため、最初は理解しづらいことがあります。

2. **深さ優先探索（DFS）の適用**: このアルゴリズムでは、ボード上の各位置から始めて、可能なすべての方向に単語を形成するための深さ優先探索を行います。DFSは再帰を使用して実装されており、再帰自体が初学者には難しいと感じることがよくあります。

3. **最適化**: このコードの特定の部分（例：`refs`）は、探索を高速化するための最適化です。最適化は一般に、基本的なアルゴリズムの理解がある場合にのみ実施されます。

初めてこのようなアルゴリズムに触れる場合、各部分を一つずつゆっくりと解析することをおすすめします。それぞれの部分がどのように動作するのか、なぜそのような実装が選ばれたのかを理解することで、全体の理解が深まるはずです。
"""