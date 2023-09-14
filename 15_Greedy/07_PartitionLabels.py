from typing import List

def partitionLabels(S: str) -> List[int]:
    count = {}
    res = []
    i, length = 0, len(S)
    for j in range(length):
        c = S[j]
        count[c] = j

    curLen = 0
    goal = 0
    while i < length:
        c = S[i]
        goal = max(goal, count[c])
        curLen += 1

        if goal == i:
            res.append(curLen)
            curLen = 0
        i += 1
    return res
 
s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))

s = "eccbbbbdec"
print(partitionLabels(s))

"""
この関数は、文字列`S`を受け取り、その文字列を部分文字列に分割するための指示を提供します。各部分文字列は、文字列内の各文字がその部分文字列内にのみ出現するように分割されるものです。関数は、各部分文字列の長さを要素として持つリストを返します。

## 大まかな説明:
文字列`S`を受け取り、その文字列を複数の部分文字列に分割します。各部分文字列は、その中に含まれる文字がその部分にのみ存在することを保証します。この関数は、各部分文字列の長さを示す整数のリストを返します。

## 部分毎の説明:

1. `count = {}`
    - 各文字が最後に現れるインデックスを保存する辞書を初期化します。

2. `for j in range(length):`
    - 文字列`S`をイテレートして、各文字の最後の位置を辞書に保存します。

3. `count[c] = j`
    - 現在の文字`c`の最後の位置を辞書に保存します。

4. `curLen = 0` と `goal = 0`
    - 現在の部分文字列の長さを保存するための変数と、目的地としてのインデックスを保存する変数を初期化します。

5. `while i < length:`
    - 文字列`S`を再度イテレートします。

6. `goal = max(goal, count[c])`
    - 現在の文字の最後の位置と、既存の目的地を比較し、大きい方を新しい目的地として保存します。

7. `if goal == i:`
    - 現在のインデックスが目的地に到達した場合、部分文字列が完了したことを示します。

8. `res.append(curLen)`
    - 完了した部分文字列の長さを結果のリストに追加します。

9. `curLen = 0`
    - 現在の部分文字列の長さをリセットします。

10. `return res`
    - 各部分文字列の長さのリストを返します。

この関数は、文字列内の各文字がどこで最後に出現するかを追跡することで、部分文字列を効率的に切り分けることができます。
"""