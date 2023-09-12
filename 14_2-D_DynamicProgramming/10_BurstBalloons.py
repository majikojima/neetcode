from typing import List

def maxCoins(nums: List[int]) -> int:
    cache = {}
    nums = [1] + nums + [1]

    for offset in range(2, len(nums)):
        for left in range(len(nums) - offset):
            right = left + offset
            for pivot in range(left + 1, right):
                coins = nums[left] * nums[pivot] * nums[right]
                coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                cache[(left, right)] = max(coins, cache.get((left, right), 0))
    return cache.get((0, len(nums) - 1), 0)

nums = [3,1,5,8]
print(maxCoins(nums))

nums = [1,5]
print(maxCoins(nums))

"""
このコードは、問題「Burst Balloons」の解答の一部であり、`nums`リストに含まれる気球を最大の得点で割る方法を探すものです。気球を割ると、割った気球の左右の隣接した気球の値との積によって得点が与えられます。

以下がコードの大まかな説明と部分ごとの説明です：

1. **初期設定**:
    - `cache = {}`: この辞書は、`nums`の異なる部分セットでの最大得点をキャッシュします。
    - `nums = [1] + nums + [1]`: 両端に`1`を追加することで、気球が割られたときの計算を簡単にします。

2. **ループを使用したダイナミックプログラミング**:
    - 外側のループ：`for offset in range(2, len(nums)):` は、考慮する気球の範囲の幅を設定します。
    - 中間のループ：`for left in range(len(nums) - offset):` は、考慮する範囲の開始点を設定します。
        - `right = left + offset`: 現在考慮中の範囲の終点を設定します。
        - 内側のループ：`for pivot in range(left + 1, right):` は、選択される気球のピボット（中心点）を設定します。

3. **得点の計算**:
    - `coins = nums[left] * nums[pivot] * nums[right]`: 現在のピボットの気球を割ることによる得点を計算します。
    - 次の2行のコードでは、割った気球の左右の部分セットからの追加の得点を計算します。

4. **最大得点の更新**:
    - `cache[(left, right)] = max(coins, cache.get((left, right), 0))`: 現在の範囲に対する最大得点を更新します。

5. **結果の返却**:
    - `return cache.get((0, len(nums) - 1), 0)`: 全体の範囲における最大得点を返します。

このアルゴリズムは、`nums`の異なる部分セットで得られる得点をキャッシュしながら、最終的な得点を計算することで、問題を効率的に解決します。
"""