class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)

        # Dynamic Programming
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]

S = Solution()
s = "12"
print(S.numDecodings(s))

s = "226"
print(S.numDecodings(s))

"""
このコードは、与えられた文字列`s`がどのように「A」から「Z」のアルファベットにデコードできるかの方法の数を求める問題を解くものです。例えば、`'226'`は、`"BZ" (2 26)`, `"VF" (22 6)`, `"BBF" (2 2 6)`の3通りにデコードできます。

### 大まかな説明
コードには2つの方法が含まれていますが、それぞれ同じ結果を生成します。
1. メモ化を使用したDFS (深さ優先探索)
2. 動的プログラミング (コメントアウトされている部分)

### 部分毎の説明

#### メモ化を使用したDFS

1. 
```python
dp = {len(s): 1}
```
`dp`はメモ化のための辞書であり、キーは文字列`s`のインデックス、値はその位置からのデコード方法の数です。初期状態として、文字列の末尾からのデコード方法は1通り（何もしない）としています。

2.
```python
def dfs(i):
```
DFSを実行するためのヘルパー関数。現在のインデックス`i`を引数として取り、その位置からのデコード方法の数を返します。

3.
```python
if i in dp:
    return dp[i]
if s[i] == "0":
    return 0
```
メモ化された結果をチェックするための条件文。そして、`"0"`は単独ではデコードできないので、その場合は0を返します。

4.
```python
res = dfs(i + 1)
```
現在の文字のみをデコードする場合の次のインデックスのデコード方法の数を取得します。

5.
```python
if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
    res += dfs(i + 2)
```
現在の文字と次の文字を組み合わせてデコードできる場合（例："12"や"24"など）、次の次のインデックスのデコード方法の数を加算します。

6.
```python
dp[i] = res
return res
```
計算した結果をメモ化し、その結果を返します。

7.
```python
return dfs(0)
```
最初のインデックスからDFSを開始して、最終結果を返します。

#### 動的プログラミング (コメントアウトされている部分)

この方法も前の方法と似ていますが、反復的なアプローチを使用しており、文字列の末尾から先頭に向かって計算を行っています。

1. 
```python
dp = {len(s): 1}
```
動的プログラミングのための辞書`dp`の初期化。

2.
```python
for i in range(len(s) - 1, -1, -1):
```
文字列の末尾から先頭に向かってループを進めます。

残りの部分は前の方法と非常に似ていて、`dp`の辞書を更新しながらデコード方法の数を計算しています。
"""

"""
文字列 `s = "12"` についてシミュレーションします。

#### メモ化を使用したDFSの場合

1. `dfs(0)` が呼び出される。
2. `i = 0` は `dp` にはまだメモ化されていないため、次に進む。
3. `s[0] = "1"` であり、これは "0" ではないため次に進む。
4. 次のインデックス、つまり `i = 1` に対して `dfs(1)` を呼び出す。
5. `i = 1` はまだメモ化されていないので、次に進む。
6. `s[1] = "2"` であり、これは "0" ではないため次に進む。
7. 次のインデックス、つまり `i = 2` に対して `dfs(2)` を呼び出す。
8. ここで `i = 2` は `dp` にメモ化されており、`1` として返る。
9. `res` は `1` になる。
10. `s[1]` と `s[2]` を組み合わせてデコードできるか確認する。しかし、`i + 1 = 2` は `len(s)` と等しいので、このステップはスキップされる。
11. `i = 1` に対する結果は `1` なので、これを `dp` にメモ化して返す。
12. `i = 0` で `s[0]` と `s[1]` を組み合わせてデコードできるかを確認。条件に合致するので、`i = 2` に対して `dfs(2)` を呼び出す。
13. 再度、`i = 2` は `1` として返る。
14. `res` は `1 + 1 = 2` に更新される。
15. `i = 0` に対する結果は `2` なので、これを `dp` にメモ化して返す。
16. 最終結果は `2`。

#### 動的プログラミングの場合

1. `dp = {2: 1}` として初期化。
2. `i = 1` からスタート。
3. `s[1] = "2"` は "0" ではないので、`dp[2] = 1` を加算して `dp[1] = 1`。
4. `i = 0` に移動。
5. `s[0] = "1"` は "0" ではないので、`dp[1] = 1` を加算して `dp[0] = 1`。
6. `s[0]` と `s[1]` を組み合わせてデコードできるか確認。条件に合致するので、`dp[2] = 1` を加算して `dp[0] = 2`。
7. 最終結果は `2`。

どちらの方法も最終的に `2` を結果として返します。
"""