def longestCommonSubsequence(text1: str, text2: str) -> int:
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]

text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))

text1 = "abc"
text2 = "abc"
print(longestCommonSubsequence(text1, text2))

text1 = "abc"
text2 = "def"
print(longestCommonSubsequence(text1, text2))

"""
このコードは、2つの文字列`text1`と`text2`の間の最長の共通部分列（LCS）の長さを求めるためのものです。ここで共通部分列とは、2つの文字列が共有する部分列で、その部分列の中の文字は、元の2つの文字列の中で同じ順序で出現しますが、連続している必要はありません。

コードの部分ごとの説明を行います：

1. **初期化**:
    ```python
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
    ```
    `dp`は2次元のリストで、`text1`の長さ+1 x `text2`の長さ+1のサイズを持っています。`dp[i][j]`は`text1`のi番目以降と`text2`のj番目以降の部分文字列の間のLCSの長さを示しています。

2. **動的計画法のループ**:
    ```python
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
    ```
    外側のループは`text1`を逆順に繰り返し、内側のループは`text2`を逆順に繰り返します。各ステップで、文字`text1[i]`と`text2[j]`を比較します。
    - 2つの文字が等しい場合、それらの文字は共通部分列の一部となり、`1 + dp[i + 1][j + 1]`として結果を更新します。
    - 2つの文字が等しくない場合、`text1`の次の文字または`text2`の次の文字との間のLCSの長さを比較し、大きい方の値を取得して結果を更新します。

3. **結果の返却**:
    ```python
    return dp[0][0]
    ```
    最後に、`dp[0][0]`は2つの文字列全体の間のLCSの長さを示しているので、それを返します。

このアルゴリズムの時間計算量は`O(len(text1) * len(text2))`であり、空間計算量も同じです。
"""