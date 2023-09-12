def change(amount: int, coins: List[int]) -> int:
    # MEMOIZATION
    # Time: O(n*m)
    # Memory: O(n*m)
    cache = {}

    def dfs(i, a):
        if a == amount:
            return 1
        if a > amount:
            return 0
        if i == len(coins):
            return 0
        if (i, a) in cache:
            return cache[(i, a)]

        cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
        return cache[(i, a)]

    return dfs(0, 0)

    # DYNAMIC PROGRAMMING
    # Time: O(n*m)
    # Memory: O(n*m)
    dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)
    for a in range(1, amount + 1):
        for i in range(len(coins) - 1, -1, -1):
            dp[a][i] = dp[a][i + 1]
            if a - coins[i] >= 0:
                dp[a][i] += dp[a - coins[i]][i]
    return dp[amount][0]

    # DYNAMIC PROGRAMMING
    # Time: O(n*m)
    # Memory: O(n) where n = amount
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(len(coins) - 1, -1, -1):
        nextDP = [0] * (amount + 1)
        nextDP[0] = 1

        for a in range(1, amount + 1):
            nextDP[a] = dp[a]
            if a - coins[i] >= 0:
                nextDP[a] += nextDP[a - coins[i]]
        dp = nextDP
    return dp[amount]

amount = 5
coins = [1,2,5]
print(change(amount, coins))

"""
このコードは、与えられたコインの組み合わせで特定の金額を作るための方法の数を計算する問題に取り組んでいます。このコードは3つの異なる方法でこの問題にアプローチしています。

### 1. メモ化を用いた再帰:
- **大まかな説明**:
  このアプローチは、再帰を使用してすべての可能なコインの組み合わせを調べますが、既に計算された結果をキャッシュするためのメモ化を使用して効率を向上させます。

- **部分毎の説明**:
  - `cache = {}`: 既に計算された結果を保存するための辞書。
  - `dfs(i, a)`: 現在のコイン `i` と現在の合計金額 `a` に基づいて再帰的に解を計算する関数。
  - `return dfs(0, 0)`: 関数の最初の呼び出し。最初のコインから開始し、合計金額は0です。

### 2. 2次元動的計画法:
- **大まかな説明**:
  2次元のDP配列を使用して、特定の金額を作成する方法の数を計算します。

- **部分毎の説明**:
  - `dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]`: 各金額とコインインデックスの組み合わせに対して方法の数を保存する2次元のDPテーブル。
  - `dp[0] = [1] * (len(coins) + 1)`: 金額が0の場合、1つの方法（コインを使用しない）しかありません。
  - 二重ループ： すべての金額とコインの組み合わせを調べます。

### 3. 1次元動的計画法:
- **大まかな説明**:
  このアプローチでは、スペースの効率性を高めるために1次元のDP配列を使用します。

- **部分毎の説明**:
  - `dp = [0] * (amount + 1)`: 各金額に対して方法の数を保存する1次元のDPテーブル。
  - `dp[0] = 1`: 金額が0の場合、1つの方法（コインを使用しない）しかありません。
  - ループ： 各コインに対して、そのコインを使用して各金額を作る方法の数を更新します。

すべてのアプローチは、時間の観点で`O(n*m)`の計算量を持っていますが、スペースの使用に違いがあります。
"""