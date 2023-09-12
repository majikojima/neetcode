def minDistance(word1: str, word2: str) -> int:
    dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

    for j in range(len(word2) + 1):
        dp[len(word1)][j] = len(word2) - j
    for i in range(len(word1) + 1):
        dp[i][len(word2)] = len(word1) - i

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
    return dp[0][0]

word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))

word1 = "intention"
word2 = "execution"
print(minDistance(word1, word2))

"""
このコードは、2つの文字列間の最小編集距離（またはLevenshtein距離とも呼ばれる）を計算するものです。最小編集距離とは、1つの文字列を別の文字列に変換するために必要な最小の単一文字の操作（挿入、削除、置換）の数を指します。

具体的な動作としては以下のとおりです：

1. **dpの初期化**： `dp`という二次元リストを初期化します。`dp[i][j]`は、`word1`の最初の`i`文字と`word2`の最初の`j`文字の最小編集距離を示します。無限大（`float("inf")`）で初期化します。

2. **境界条件の設定**： 
   - 各文字列の終端に対して、もう1つの文字列の残りの部分を削除することで変換を完了する距離を設定します。
   - 例: `dp[len(word1)][j]`は`word1`が終了した後の`word2`の残りの部分を削除するのに必要な操作の数を示します。

3. **ダブルループを使用したDPの計算**：
   - 外側のループは`word1`の文字を逆順にイテレートします。
   - 内側のループは`word2`の文字を逆順にイテレートします。
   - 現在の`i`と`j`の位置の文字が一致する場合、`dp[i + 1][j + 1]`の値をコピーします（変更不要）。
   - 一致しない場合、次の3つの操作から最小の操作を選択します：
     1. `dp[i + 1][j]`（削除）
     2. `dp[i][j + 1]`（挿入）
     3. `dp[i + 1][j + 1]`（置換）

4. **結果の返却**： 最後に、`dp[0][0]`を返します。これは、全体の`word1`と`word2`間の最小編集距離を示します。

部分的なコードの説明：

- `dp = [[float("inf")] * ...`: `word1`と`word2`の長さに基づいて`dp`リストを初期化します。
- `for j in range(len(word2) + 1):`と`for i in range(len(word1) + 1):`: 境界条件の設定部分です。
- `for i in range(len(word1) - 1, -1, -1):`: `word1`の文字を逆順にイテレートするループ。
- `for j in range(len(word2) - 1, -1, -1):`: `word2`の文字を逆順にイテレートするループ。
- `if word1[i] == word2[j]:`: 現在の文字が一致するかどうかを確認します。
- `else: ...`: 現在の文字が一致しない場合、最小の編集操作を探します。

このコードは、動的プログラミングを使用して、効率的に2つの文字列間の最小編集距離を計算します。
"""