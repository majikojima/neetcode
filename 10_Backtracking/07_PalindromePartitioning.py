from typing import List

def partition(s: str) -> List[List[str]]:
    res, part = [], []

    def dfs(i):
        if i >= len(s):
            res.append(part[:])
            return
        for j in range(i, len(s)):
            if isPali(s, i, j):
                part.append(s[i : j + 1])
                dfs(j + 1)
                part.pop()

    dfs(0)
    return res

def isPali(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True

s = "aab"
print(partition(s))
s = "aa"
print(partition(s))

"""
このコードは、与えられた文字列`s`を回文の部分文字列に分割するすべての可能な方法を生成します。

### 大まかな説明
文字列`s`が与えられたとき、このコードは`s`を回文の部分文字列に分割するすべての可能な方法を見つけます。再帰的な深さ優先探索(DFS)を使用して、すべての可能な分割を試み、その結果をリストとして返します。

### 部分ごとの詳細説明

1. `res, part = [], []`:
    - `res`: 最終的な結果のリスト。回文の部分文字列のリストのリストとして表現されます。
    - `part`: 現在の分割候補。

2. `dfs(i)`:
    - 再帰的な補助関数。指定されたインデックス`i`から`s`を探索して、回文の部分文字列に分割します。

3. `if i >= len(s)`:
    - 基底条件。文字列の末尾に達した場合、`part`を`res`に追加します。

4. `for j in range(i, len(s))`:
    - `i`から始まるすべての部分文字列を探索するループ。

5. `if self.isPali(s, i, j)`:
    - `isPali`関数を使用して、`s[i:j+1]`が回文であるかどうかを確認します。

6. `part.append(s[i : j + 1])`:
    - `s[i:j+1]`が回文である場合、それを`part`リストに追加します。

7. `dfs(j + 1)`:
    - 次の部分文字列を探索するための再帰的な呼び出し。

8. `part.pop()`:
    - 現在の選択を取り消し、次の可能性を探索します。

9. `isPali(s, l, r)`:
    - 文字列`s`のサブセット`s[l:r+1]`が回文であるかどうかを確認する補助関数。

10. `while l < r`:
    - 与えられた範囲内で文字列の左端と右端を比較し、それらが一致するかどうかを確認するループ。

この関数は、与えられた文字列を回文の部分文字列に分割するすべての方法を効率的に生成します。
"""
