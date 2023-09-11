from typing import List

def maxProduct(nums: List[int]) -> int:
    # O(n)/O(1) : Time/Memory
    res = nums[0]
    curMin, curMax = 1, 1

    for n in nums:
        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res

nums = [2,3,-2,4]
print(maxProduct(nums))

nums = [-2,0,-1]
print(maxProduct(nums))

"""
このコードは、与えられた整数のリストの中で連続する部分配列の積の最大値を求めるためのものです。具体的には、このアルゴリズムは動的計画法のアプローチを採用しており、リスト全体を一度だけスキャンして問題を解決します。

コード全体の大まかな説明:
- 与えられた整数のリストから、最大の部分配列の積を求める。
- 各要素を順に処理しながら、その要素を終点とする部分配列の中での最大値と最小値を維持します。
- この最大値と最小値を用いることで、次の要素を処理する際に、その要素を終点とする部分配列の積の最大値と最小値を効率的に計算できます。

部分ごとの詳しい説明:

1. `res = nums[0]`
   - `res` は最終的な結果（最大の部分配列の積）を保存するための変数です。初期値としてリストの最初の要素を設定します。

2. `curMin, curMax = 1, 1`
   - `curMin` と `curMax` は、現在の要素を終点とする部分配列の積の最小値と最大値をそれぞれ保存するための変数です。
   - 初期値として 1 が設定されています。

3. `for n in nums:`
   - リストの各要素を順に処理します。

4. `tmp = curMax * n`
   - 現在の要素を終点とする部分配列の積の最大値の計算の一部として、一時的な値を計算します。

5. `curMax = max(n * curMax, n * curMin, n)`
   - 現在の要素を終点とする部分配列の積の最大値を更新します。
   - これは、前の要素までの最大の積と現在の要素との積、前の要素までの最小の積と現在の要素との積、現在の要素そのものの3つの値の中から最大のものを選ぶことで計算されます。

6. `curMin = min(tmp, n * curMin, n)`
   - 現在の要素を終点とする部分配列の積の最小値を更新します。

7. `res = max(res, curMax)`
   - 最終的な結果を更新します。

8. `return res`
   - 最終的な結果を返します。

このアルゴリズムの鍵となるのは、負の数との乗算の際に最大値と最小値が入れ替わる可能性があるため、`curMax` と `curMin` の両方を維持している点です。
"""

"""
`nums = [2,3,-2,4]` でのシミュレーションを行います。

初期状態:
```
res = 2
curMin = 1
curMax = 1
```

1. `n = 2` (最初の要素)
```
tmp = curMax * n = 1 * 2 = 2
curMax = max(2 * 2, 2 * 1, 2) = 4
curMin = min(2, 1 * 2, 2) = 2
res = max(2, 4) = 4
```
この時点での状態:
```
res = 4
curMin = 2
curMax = 4
```

2. `n = 3` (2つ目の要素)
```
tmp = curMax * n = 4 * 3 = 12
curMax = max(4 * 3, 2 * 3, 3) = 12
curMin = min(12, 2 * 3, 3) = 3
res = max(4, 12) = 12
```
この時点での状態:
```
res = 12
curMin = 3
curMax = 12
```

3. `n = -2` (3つ目の要素)
```
tmp = curMax * n = 12 * (-2) = -24
curMax = max(12 * (-2), 3 * (-2), -2) = -2
curMin = min(-24, 3 * (-2), -2) = -24
res = max(12, -2) = 12
```
この時点での状態:
```
res = 12
curMin = -24
curMax = -2
```

4. `n = 4` (4つ目の要素)
```
tmp = curMax * n = -2 * 4 = -8
curMax = max(-2 * 4, -24 * 4, 4) = 4
curMin = min(-8, -24 * 4, 4) = -96
res = max(12, 4) = 12
```
この時点での状態:
```
res = 12
curMin = -96
curMax = 4
```

最終的に、`res = 12` となります。よって、このリストにおける連続する部分配列の積の最大値は 12 です。
"""