class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
print(obj.insert("apple"))
print(obj.search("app"))
print(obj.search("apple"))
print(obj.startsWith("l"))
print(obj.startsWith("app"))
print(obj.insert("app"))
print(obj.search("app"))

"""
このコードは、`Trie`というデータ構造を表現しています。Trie（またはプレフィックスツリー）は、特に文字列検索を高速に行うためのデータ構造です。

**大まかな説明**:
この`Trie`クラスは、アルファベットの小文字の単語を格納・検索・接頭辞での検索をサポートしています。

---

**部分毎の説明**:

1. **TrieNodeクラス**:
    - このクラスはTrieのノードを表しています。
    - `children`: 各ノードは26の子ノードへの参照を持っており（英語の小文字のため）、初期化時には全て`None`に設定されます。
    - `end`: 単語がこのノードで終わる場合は`True`、そうでない場合は`False`。単語の終端を示します。

2. **Trieクラス**:
    - `__init__`: Trieの初期化。ルートノードを生成します。
    - `insert`: 与えられた単語をTrieに挿入します。
        - 文字ごとにTrieをトラバースし、必要ならば新しいノードを生成します。
        - 単語の最後に到達したら、そのノードの`end`を`True`に設定します。
    - `search`: 与えられた単語がTrieに存在するかを返します。
        - 文字ごとにTrieをトラバースします。
        - 途中でノードが存在しない、または単語の終端まで達してそのノードの`end`が`False`の場合、`False`を返します。
    - `startsWith`: 与えられた接頭辞を持つ任意の単語がTrieに存在するかを返します。
        - 接頭辞の文字ごとにTrieをトラバースします。
        - 途中でノードが存在しない場合、`False`を返します。

各関数では、与えられた文字列の各文字に対してASCIIコードから`ord("a")`を減算することで、アルファベットの小文字のインデックス（0-25）を取得しています。このインデックスは、`children`配列での位置を示しています。
"""

"""
はい、おっしゃる通りです。Trie（またはプレフィックスツリー）は、特定の種類の検索タスク、特に文字列の検索や自動補完のようなタスクで非常に効率的に動作する高度なデータ構造の1つです。

`TrieNode`の中での定義を少し深堀りします：

1. **children**: 
    - これは、26の`TrieNode`の参照（またはポインタ）を保持するリストです。それぞれの参照は、アルファベットの各文字（a-z）に対応しています。 
    - `None`は、その文字に対応する子ノードが存在しないことを示しています。
    - 例えば、`children[0]`は文字'a'に対応し、`children[25]`は'z'に対応します。

2. **end**: 
    - これはブールフラグで、ノードが文字列の終端（つまり、ツリー内の実際の単語の終わり）を示しているかどうかを示します。

実際には、このデータ構造を構築して操作する方法を知っていれば、それを実装するのはそこまで難しくありません。しかし、このデータ構造をゼロから考えるのは確かに難しいです。多くのアルゴリズムやデータ構造は、過去の研究や実践に基づいて時間をかけて開発されてきました。ですので、それらを学ぶときは、どのように動作するかを理解し、何のために有用であるかを知ることが重要です。
"""

"""
シミュレーションの実行を開始します。

1. Trieのインスタンス`obj`を作成します。
2. "apple"をTrieに挿入します。
   - 挿入の進行：
     - a -> p -> p -> l -> e
   - すべての文字がTrieに正常に挿入されます。
   - `insert`メソッドは`None`を返すため、`print(obj.insert("apple"))`は`None`を出力します。
3. "app"がTrieに存在するか検索します。
   - 検索の進行：
     - a -> p -> p
   - "app"の終端は`end = False`であるため、`search`メソッドは`False`を返します。
   - `print(obj.search("app"))`は`False`を出力します。
4. "apple"がTrieに存在するか検索します。
   - 検索の進行：
     - a -> p -> p -> l -> e
   - "apple"の終端は`end = True`であるため、`search`メソッドは`True`を返します。
   - `print(obj.search("apple"))`は`True`を出力します。
5. 任意の単語が"l"で始まるか検索します。
   - "l"はTrieのルート直下に存在しないため、`startsWith`メソッドは`False`を返します。
   - `print(obj.startsWith("l"))`は`False`を出力します。
6. 任意の単語が"app"で始まるか検索します。
   - 検索の進行：
     - a -> p -> p
   - "app"はTrieに存在するため、`startsWith`メソッドは`True`を返します。
   - `print(obj.startsWith("app"))`は`True`を出力します。
7. "app"をTrieに挿入します。
   - 挿入の進行：
     - a -> p -> p
   - すべての文字がTrieに正常に挿入されます。
   - "app"の終端の`end`フラグを`True`に設定します。
   - `insert`メソッドは`None`を返すため、`print(obj.insert("app"))`は`None`を出力します。
8. 再度"app"がTrieに存在するか検索します。
   - 今回、"app"の終端の`end`フラグは`True`であるため、`search`メソッドは`True`を返します。
   - `print(obj.search("app"))`は`True`を出力します。

シミュレーションの出力結果：

```
None
False
True
False
True
None
True
```
"""