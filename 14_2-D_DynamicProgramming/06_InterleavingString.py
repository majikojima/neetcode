def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
    dp[len(s1)][len(s2)] = True

    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                dp[i][j] = True
            if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                dp[i][j] = True
    return dp[0][0]

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(isInterleave(s1, s2, s3))

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(isInterleave(s1, s2, s3))

"""
このコードは、文字列`s1`と`s2`が交互に文字を取ることで文字列`s3`を形成できるかどうかを確認するものです。具体的には以下のように動作します：

1. **文字列の長さの確認**: 最初に、`s1`と`s2`の合計の長さが`s3`の長さと一致しない場合は、`s3`は`s1`と`s2`の交差によって生成されることはないので、`False`を返します。

2. **dpの初期化**: `dp`という二次元リストを初期化します。`dp[i][j]`は、`s1`の最初の`i`文字と`s2`の最初の`j`文字が交互に`s3`の最初の`i+j`文字を形成できるかどうかを示します。`dp[len(s1)][len(s2)]`は`s3`の終端を意味するので、`True`として設定されます。

3. **ダブルループを使ったDPの計算**:
   - 外側のループは`s1`の文字を逆順にイテレートします。
   - 内側のループは`s2`の文字を逆順にイテレートします。
   - 現在の`i`と`j`の位置の文字が`s3`の対応する位置の文字と一致するかどうかを確認します。
   - その後、次の`dp`位置（右または下）から値を取得して、現在の`dp`の位置を更新します。

4. **結果の返却**: 最後に、`dp[0][0]`を返します。これは、`s1`と`s2`の全文字が`s3`を形成できるかどうかを示します。

具体的なコードの部分の説明：

- `dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]`: `s1`の長さ+1と`s2`の長さ+1の二次元リストを`False`で初期化します。
- `dp[len(s1)][len(s2)] = True`: 最後の位置を`True`に設定します。
- `for i in range(len(s1), -1, -1)`: `s1`の文字を逆順にイテレートするループ。
- `for j in range(len(s2), -1, -1)`: `s2`の文字を逆順にイテレートするループ。
- `if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:`: 現在の`s1`の文字が`s3`の対応する位置の文字と一致するかどうかを確認します。
- `if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:`: 現在の`s2`の文字が`s3`の対応する位置の文字と一致するかどうかを確認します。

最後に、`dp[0][0]`を返すことで、全体の文字列`s1`と`s2`が`s3`を形成できるかどうかを示します。
"""