def isValid(s: str) -> bool:
    Map = {")": "(", "}": "{", "]": "["}
    stack = []
    for c in s:
        if c not in Map:
            stack.append(c)
            continue
        if not stack:
            return False
        if Map[c] != stack[-1]:
            return False
        stack.pop()
    return not stack

s = "()[]{}"
print(isValid(s))

"""
指示されたコードの一部は、多くのプログラミング言語でリストやスタックの操作を示すものに似ていますが、Pythonの文法を基に説明します。

1. `stack.append(c)`:
   - `append()`はPythonのリストに要素を追加するメソッドです。この例では、`stack`という名前のリストの末尾に`c`という変数の値を追加しています。

2. `stack.pop()`:
   - `pop()`はPythonのリストから最後の要素を削除するメソッドです。この要素を戻り値として返します。したがって、`stack.pop()`は`stack`の最後の要素を削除し、その要素を返します。

3. `stack[-1]`:
   - Pythonのリストのインデックスは、0から始まります。しかし、負のインデックスはリストの末尾から要素を参照します。`stack[-1]`は`stack`の最後の要素を参照しますが、この要素を削除するわけではありません。

例えば、`stack = [1, 2, 3]`というリストがある場合:

- `stack.append(4)`を実行すると、`stack`は`[1, 2, 3, 4]`となります。
- `stack.pop()`を実行すると、`4`が戻り値として返され、`stack`は再び`[1, 2, 3]`となります。
- `stack[-1]`を評価すると、`3`が返されますが、`stack`の内容は変わりません。
"""