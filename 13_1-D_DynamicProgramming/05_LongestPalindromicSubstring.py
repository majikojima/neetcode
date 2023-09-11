def longestPalindrome(s: str) -> str:
    res = ""
    resLen = 0

    for i in range(len(s)):
        # odd lenght
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        # even lenght
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
            
    return res

s = "babad"
print(longestPalindrome(s))

s = "cbbd"
print(longestPalindrome(s))

"""
このコードは、入力文字列`s`の中で最も長い回文部分文字列（palindromic substring）を探して返すものです。回文とは、前から読んでも後ろから読んでも同じ文字列のことを指します（例：「madam」や「racecar」など）。

コードの詳細については以下の通りです。

### 大まかな説明
文字列`s`の各文字を中心として、両方向に拡張して回文を探索します。このとき、奇数の長さと偶数の長さの2種類の回文の可能性を考慮します。最も長い回文を見つけるたびに、結果を更新していきます。

### 部分毎の説明

1. 
```python
res = ""
resLen = 0
```
これは、見つけた最長の回文文字列とその長さを保存するための変数です。

2. 
```python
for i in range(len(s)):
```
文字列`s`の各文字を中心として回文を探索するためのループです。

3. 
```python
# odd length
l, r = i, i
while l >= 0 and r < len(s) and s[l] == s[r]:
```
奇数の長さの回文を探すための部分です。中心を`i`とし、`l`と`r`を左右に1つずつ移動させながら`s[l]`と`s[r]`が同じかどうかをチェックします。同じであれば回文の可能性があります。

4. 
```python
if (r - l + 1) > resLen:
    res = s[l : r + 1]
    resLen = r - l + 1
```
新しく見つけた回文の長さがこれまでの最長よりも長い場合、結果を更新します。

5. 
```python
# even length
l, r = i, i + 1
while l >= 0 and r < len(s) and s[l] == s[r]:
```
偶数の長さの回文を探すための部分です。このケースでは、`i`の次の文字も中心に考慮するため、`r = i + 1`としています。

このアプローチは、各文字に対して左右に拡張していくため、`O(n^2)`の時間複雑度を持つことに注意してください。
"""