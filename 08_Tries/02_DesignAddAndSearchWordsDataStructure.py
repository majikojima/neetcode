class TrieNode:
    def __init__(self):
        self.children = {} # a : TrieNode
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))
print(obj.search("dad"))
print(obj.search(".ad"))
print(obj.search("m.."))

"""
こちらは、文字列の集合を効率的に格納・検索するためのデータ構造「Trie（トライ木）」を基にしたクラスの定義です。特に、ワイルドカード文字（`.`）を用いた検索をサポートしています。

**1. TrieNodeクラス**:
このクラスは、Trie（トライ木）のノードを表現します。

- `self.children`: 子ノードへの参照を格納する辞書。キーは文字、値はその文字に対応する`TrieNode`オブジェクトです。
- `self.word`: このノードが単語の終わりを示す場合は`True`、そうでない場合は`False`。

**2. WordDictionaryクラス**:
このクラスは、単語の辞書をTrieの形式で格納する機能を提供します。

- `__init__(self)`: 初期化メソッドで、ルートノードを作成します。
- `addWord(self, word: str) -> None`: 単語をTrieに追加するメソッド。
    - wordの各文字をルートから順にたどり、存在しない文字のノードを新たに作成します。
    - 単語の終わりのノードの`word`属性を`True`に設定します。
- `search(self, word: str) -> bool`: 指定された単語（またはワイルドカードを含むパターン）がTrieに存在するかどうかを検索します。
    - `dfs(j, root)`という内部関数（デプスファーストサーチを意味する）を使用しています。
    - この関数は再帰的に呼び出され、`.`（ワイルドカード）が見つかった場合には、すべての子ノードに対してその関数を再帰的に呼び出します。
    - 普通の文字が見つかった場合は、その文字が現在のノードの子として存在するかどうかをチェックします。
    - 単語の終わりまで進んだら、現在のノードが実際の単語の終わりを示すかどうか（`cur.word`が`True`かどうか）を確認します。

このデータ構造は、文字列の集合を格納し、特定のパターンが存在するかどうかを高速に検索することができます。
"""

"""
Trieを用いたこの検索の実装で、`dfs`（デプスファーストサーチ）を使用するのは、ワイルドカード文字`.`が存在する場合に、任意の文字にマッチさせる必要があるからです。

具体的には、`.`が見つかった時、`dfs`を使用して現在のノードのすべての子ノードを再帰的に探索します。これにより、`.`がどの文字ともマッチするという動作を実現しています。

以下はその部分のコードを詳細に説明します：

```python
if c == ".":
    for child in cur.children.values():
        if dfs(i + 1, child):
            return True
    return False
```

- `c == "."`：もし現在の文字が`.`（ワイルドカード）であれば、
- `for child in cur.children.values()`: 現在のノードのすべての子ノードに対して、
- `if dfs(i + 1, child)`: 次の文字位置とその子ノードを基に、再び`dfs`を呼び出す。これにより、`.`に続く文字列が子ノード以下に存在するかを再帰的に検索します。
- もし何らかの子ノードでマッチする文字列が見つかった場合（`dfs(i + 1, child)`が`True`を返した場合）、この`dfs`も`True`を返す。
- すべての子ノードでマッチしなかった場合、この`dfs`は`False`を返します。

この動きを実現するために、再帰的な探索である`dfs`を使用しています。
"""

"""
了解しました。`WordDictionary`クラスを使って、"mad"という単語を追加し、"m.."というパターンで検索するシミュレーションを行います。

まず、初期状態では Trie は空です。

```
obj = WordDictionary()
```

次に、"mad"という単語を追加します。

```
obj.addWord("mad")
```

Trieは以下のようになります。

```
root
|
m - a - d
```

最後に、"m.."というパターンで検索します。

```
print(obj.search("m.."))
```

1. `m`の部分はノードとして存在しているので、次の文字へ進みます。
2. 次の文字は`.`です。このワイルドカードは任意の文字にマッチします。現在のノード`m`には子ノード`a`がありますので、それにマッチすると判断して、次の文字へ進みます。
3. 次の文字も`.`です。このワイルドカードは再び任意の文字にマッチします。現在のノード`a`には子ノード`d`がありますので、それにマッチすると判断します。
4. 全ての文字を検討し終え、さらに最後のノードが単語の終端を示す`word=True`となっているため、マッチすると結論され、`True`が返されます。

したがって、`print(obj.search("m.."))`は`True`を出力します。
"""

"""
了解しました。`WordDictionary`クラスを使って、"mad"という単語を追加し、"m.."というパターンで検索するシミュレーションを行います。

まず、初期状態では Trie は空です。

```
obj = WordDictionary()
```

次に、"mad"という単語を追加します。

```
obj.addWord("mad")
```

Trieは以下のようになります。

```
root
|
m - a - d
```

最後に、"m.."というパターンで検索します。

```
print(obj.search("m.."))
```

1. `m`の部分はノードとして存在しているので、次の文字へ進みます。
2. 次の文字は`.`です。このワイルドカードは任意の文字にマッチします。現在のノード`m`には子ノード`a`がありますので、それにマッチすると判断して、次の文字へ進みます。
3. 次の文字も`.`です。このワイルドカードは再び任意の文字にマッチします。現在のノード`a`には子ノード`d`がありますので、それにマッチすると判断します。
4. 全ての文字を検討し終え、さらに最後のノードが単語の終端を示す`word=True`となっているため、マッチすると結論され、`True`が返されます。

したがって、`print(obj.search("m.."))`は`True`を出力します。
"""