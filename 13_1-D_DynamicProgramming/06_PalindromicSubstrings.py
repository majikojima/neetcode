class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

S = Solution()
s = "abc"
print(S.countSubstrings(s))

s = "aaa"
print(S.countSubstrings(s))

"""
このコードは、文字列`s`内に存在するすべての回文部分文字列の数をカウントするものです。

### 大まかな説明
文字列`s`の各文字を中心として、左右に広がって回文を探索します。このとき、奇数の長さと偶数の長さの2つの回文のパターンを考慮します。

### 部分毎の説明

1. 
```python
res = 0
```
回文部分文字列のカウント数を保存するための変数を初期化します。

2. 
```python
for i in range(len(s)):
    res += self.countPali(s, i, i)
    res += self.countPali(s, i, i + 1)
```
文字列`s`の各文字に対して、2つのパターンの回文を探索します。  
- `self.countPali(s, i, i)`は`i`を中心とする奇数長の回文を探索します。例：`aba`, `ccc`など
- `self.countPali(s, i, i + 1)`は`i`と`i+1`を中心とする偶数長の回文を探索します。例：`aa`, `cc`など

3. 
```python
def countPali(self, s, l, r):
    res = 0
```
与えられた中心を基に回文を探索し、その回文の数をカウントするためのヘルパー関数を定義します。

4. 
```python
while l >= 0 and r < len(s) and s[l] == s[r]:
    res += 1
    l -= 1
    r += 1
```
左のインデックス`l`と右のインデックス`r`を使用して、文字列の外側に達するか、左右の文字が一致しなくなるまで回文を探索します。回文を見つけるたびに、結果のカウンター`res`を増やします。

最終的に、`countSubstrings`関数は`s`内のすべての回文部分文字列の数を返します。
"""