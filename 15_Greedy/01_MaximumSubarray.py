from typing import List

def maxSubArray(nums: List[int]) -> int:
    res = nums[0]

    total = 0
    for n in nums:
        total += n
        res = max(res, total)
        if total < 0:
            total = 0
    return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

nums = [1]
print(maxSubArray(nums))

nums = [5,4,-1,7,8]
print(maxSubArray(nums))

nums = [-1, -2]
print(maxSubArray(nums))

"""
このコードは、配列の連続する部分配列の合計の最大値を返す問題を解くためのものです。これは、Kadaneのアルゴリズムとして知られる方法を使用しています。

**大まかな説明**:
配列`nums`の連続する部分配列の合計の最大値を探します。それを実現するために、配列を左から右へと1つずつスキャンしていき、それまでの部分の最大値を更新していきます。この最大値は、最終的な答えとして返されます。

**部分毎の説明**:

1. `res = nums[0]`
   - `res`は、最大の部分配列の合計として初期化されます。始めは、最初の要素で初期化されています。

2. `total = 0`
   - `total`は、現在の部分配列の合計を保持する変数です。

3. `for n in nums:`
   - `nums`配列を1つずつスキャンしていきます。

4. `total += n`
   - `n`を`total`に加算して、現在の部分配列の合計を更新します。

5. `res = max(res, total)`
   - `res`を、それ自体と`total`の大きい方で更新します。これにより、最大の部分配列の合計を継続的に追跡しています。

6. `if total < 0:`
   - もし`total`が0未満であれば、それは新しい部分配列のスタート地点として有望でないことを意味します。この理由は、負の合計を持つ部分配列が、その後の要素を足しても最大値を構築するのに役立たないためです。

7. `total = 0`
   - `total`を0にリセットして、新しい部分配列のスキャンを開始します。

8. `return res`
   - これまでのスキャン中に見つけた最大の部分配列の合計を返します。

このアルゴリズムの計算量はO(n)です。これは、配列の各要素を1回だけ訪れるためです。
"""