# [https://leetcode.com/problems/valid-parentheses/]

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            print(f"stack: {stack}")
            print(f"c: {c}")
            if c not in Map:
                stack.append(c)
                continue
            print(Map[c])
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
    
s = Solution()
st = "({[]})"
result = s.isValid(st)
print(result)

"""
このコードは、括弧の組み合わせが正しい（すなわち、開く括弧と閉じる括弧が適切にペアになっている）かどうかを確認するものです。

```python
class Solution:
```
新しいクラス`Solution`を定義します。

```python
    def isValid(self, s: str) -> bool:
```
文字列`s`を引数に取り、その括弧の組み合わせが有効かどうかを返すメソッド`isValid`を定義します。

```python
        Map = {")": "(", "]": "[", "}": "{"}
```
閉じ括弧をキーとし、対応する開き括弧を値とする辞書`Map`を作成します。

```python
        stack = []
```
開いた括弧を保存するためのスタック（リスト）を初期化します。

```python
        for c in s:
```
引数の文字列`s`の各文字`c`についてループを行います。

```python
            if c not in Map:
```
現在の文字`c`が閉じ括弧でない（つまり、開き括弧である）場合は、

```python
                stack.append(c)
```
その括弧をスタックに追加します。

```python
                continue
```
次の文字に進みます。

```python
            if not stack or stack[-1] != Map[c]:
```
スタックが空であるか、またはスタックの一番上（最後）の括弧が現在の閉じ括弧`c`と対応しない開き括弧である場合は、

```python
                return False
```
無効な組み合わせであると判断し、`False`を返します。

```python
            stack.pop()
```
スタックの一番上の括弧を取り除きます（対応する閉じ括弧が見つかったため）。

```python
        return not stack
```
全ての文字を処理した後、スタックが空（全ての開き括弧に対応する閉じ括弧が見つかった）であれば`True`を返し、そうでなければ`False`を返します。
"""

"""
`if c not in Map:`というコードは、このように理解できます：「もし"c"（この場合は、テキストの各文字を指します）が"Map"という名前の箱の中になければ」

ここで、"Map"という箱は特殊な箱で、閉じ括弧（")"、"]"、"}"）を開き括弧（"("、"["、"{"）に変える魔法の箱と考えることができます。したがって、「もし"c"がこの魔法の箱の中にない」は、「もし"c"が閉じ括弧でない」つまり「"c"が開き括弧である」という意味になります。

この行のコードの目的は、「もし"c"が開き括弧だったら」その後の処理を行う、ということを判断するためのものです。具体的には、開き括弧が見つかったら、それをスタック（保存のための積み重ね）に加える、という処理を行います。

分かりやすい例えとして、例えば、友達と一緒にカードゲームをしていて、特定のカード（この場合、閉じ括弧に該当）を引いたときだけ特別なアクションをするというルールがあるとします。その特定のカードが出た時にだけ、特別なアクションをするのと同じように、このコードも特定の文字（ここでは開き括弧）が出たときだけ、特別なアクション（スタックに追加する）を行っているのです。
"""