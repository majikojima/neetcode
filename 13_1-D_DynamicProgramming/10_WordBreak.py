from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    return dp[0]

s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s, wordDict))

s = "applepenapple"
wordDict = ["apple","pen"]
print(wordBreak(s, wordDict))

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(wordBreak(s, wordDict))

"""
このコードは、与えられた文字列`s`が、`wordDict`に含まれる単語の連続として作成できるかどうかを確認するためのものです。例えば、`s = "leetcode"`、`wordDict = ["leet", "code"]`の場合、`leetcode`は`wordDict`の単語"leet"と"code"を連結して作成できるので、この関数は`True`を返します。

以下は各部分の詳細な説明です。

1. `dp = [False] * (len(s) + 1)`
   - `dp`という名前の動的プログラミングテーブルを作成します。`dp[i]`が`True`である場合、文字列`s`の`i`番目から最後までの部分文字列は`wordDict`の単語の連続として作成できることを意味します。

2. `dp[len(s)] = True`
   - 空文字列は常に分解できると考えられるため、最後の位置を`True`に設定します。

3. `for i in range(len(s) - 1, -1, -1):`
   - 逆順に`s`を繰り返します。これにより、文字列の後ろから前に向かって、各部分文字列が`wordDict`の単語の連続として作成できるかどうかを確認します。

4. `for w in wordDict:`
   - 各単語`w`に対して、それが現在のインデックス`i`から始まる部分文字列と一致するかどうかを確認します。

5. `if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:`
   - 現在のインデックスから単語`w`の長さ分だけの部分文字列が`s`に存在し、その部分文字列が`w`と一致する場合にこの条件は`True`になります。

6. `dp[i] = dp[i + len(w)]`
   - 一致する単語`w`が見つかった場合、その単語を使用して`s`を分解することが可能であるかどうかを確認するため、`dp`の対応する位置を更新します。

7. `if dp[i]: break`
   - `s`の任意の部分文字列が`wordDict`の単語の連続として分解できる場合、ループを抜けます。

最終的に、`dp[0]`が`True`であれば、文字列`s`全体が`wordDict`の単語の連続として分解できることを意味します。それ以外の場合、`False`を返します。
"""