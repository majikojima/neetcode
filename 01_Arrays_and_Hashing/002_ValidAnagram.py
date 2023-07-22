# [https://leetcode.com/problems/valid-anagram/]

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        constS, constT = {}, {}

        for i in range(len(s)):
            constS[s[i]] = 1 + constS.get(s[i], 0)
            constT[t[i]] = 1 + constT.get(t[i], 0)
        print(constS)
        return True
    
sol = Solution()
s = "anagram"
t = "managra"
result = sol.isAnagram(s, t)
print(result)

"""
もちろんです。以下に、各行について説明します。

```python
class Solution:
```
新しいクラス`Solution`を定義しています。このクラスには、異なる解法や問題の答えを含むメソッドを追加できます。

```python
    def isAnagram(self, s: str, t: str) -> bool:
```
`isAnagram`というメソッドを定義しています。このメソッドは2つの文字列`s`と`t`を引数に取り、それらがアナグラム（文字の順番を変えることで得られる別の単語）であるかどうかを判定します。返り値の型は`bool`（ブール型、つまり真偽値）です。

```python
        if len(s) != len(t):
            return False
```
まず、`s`と`t`の長さが異なる場合、それらはアナグラムにはなり得ませんので、`False`を返します。

```python
        constS, constT = {}, {}
```
`s`と`t`の各文字の出現回数をカウントするための辞書`constS`と`constT`を初期化します。

```python
        for i in range(len(s)):
```
文字列`s`の各文字についてのループを開始します。

```python
            constS[s[i]] = 1 + constS.get(s[i], 0)
```
現在の文字`s[i]`の出現回数を1増やします。もし`s[i]`が`constS`に存在しない場合は、`.get()`メソッドが`0`を返すので、出現回数は`1`になります。

```python
            constT[t[i]] = 1 + constT.get(t[i], 0)
```
同様に、文字列`t`の現在の文字`t[i]`の出現回数を1増やします。

```python
        return constS == constT
```
最後に、`s`と`t`の文字の出現回数が全て一致しているかどうか（つまり、`constS`と`constT`が等しいかどうか）を返します。もし全て一致していれば、`s`と`t`はアナグラムであると言えます。
"""