# BOTTOM-UP Dynamic Programming
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        cache[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j + 1) < len(p) and p[j + 1] == "*":
                    cache[i][j] = cache[i][j + 2]
                    if match:
                        cache[i][j] = cache[i + 1][j] or cache[i][j]
                elif match:
                    cache[i][j] = cache[i + 1][j + 1]

        return cache[0][0]


# TOP DOWN MEMOIZATION
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (  # dont use *
                    match and dfs(i + 1, j)
                )  # use *
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)

S = Solution()
s = "aa"
p = "a"
print(S.isMatch(s, p))

s = "aa"
p = "a*"
print(S.isMatch(s, p))

"""
このコードは、正規表現のパターンマッチングを行うためのものです。入力文字列`s`が、正規表現パターン`p`にマッチするかどうかを判断します。ここで、パターン`p`は、任意の文字を表す`.`と、0回以上の繰り返しを表す`*`の2つの特殊文字を持っています。

**1. BOTTOM-UP Dynamic Programming**

このアプローチでは、解を直接計算するのではなく、小さい問題から始めて、その結果を利用して大きな問題を解決します。

- `cache`: 文字列`s`とパターン`p`の各インデックス間のマッチ結果を格納するための2次元リスト。
- 初期設定: `cache[len(s)][len(p)] = True`は、空の文字列が空のパターンと一致することを示します。
- メインのループでは、文字列`s`とパターン`p`の末尾から開始して、各文字が一致するかどうかを判断します。
- `match`は、現在の文字が一致するかどうかを示すブール値です。
- `*`の処理は特別で、前の文字とともに解釈され、0回以上の繰り返しを意味します。

**2. TOP DOWN MEMOIZATION**

このアプローチは、大きな問題を小さな部分問題に分解して解決します。計算結果は`cache`に保存され、再計算を避けるために再利用されます。

- `cache`: 既に計算された部分問題の結果をキャッシュする辞書。
- `dfs(i, j)`: `s`の`i`番目と`p`の`j`番目の位置から始まる部分文字列と部分パターンがマッチするかどうかを再帰的に判断します。
- 同様に、`match`は現在の文字が一致するかどうかを示します。
- `*`の処理も同様に特別で、前の文字とともに解釈されます。

**どちらのアプローチも、文字列`s`が正規表現パターン`p`にマッチするかどうかを判断するためのものですが、計算の方法が異なります。**
"""