from typing import List

def canPartition(nums: List[int]) -> bool:
    if sum(nums) % 2:
        return False

    dp = set()
    dp.add(0)
    target = sum(nums) // 2

    for i in range(len(nums) - 1, -1, -1):
        nextDP = set()
        for t in dp:
            if (t + nums[i]) == target:
                return True
            nextDP.add(t + nums[i])
            nextDP.add(t)
        dp = nextDP
    return False

nums = [1,5,11,5]
print(canPartition(nums))

nums = [1,2,3,5]
print(canPartition(nums))

"""
このコードは、与えられた数字のリスト`nums`を2つのサブセットに分割できるかどうかを判定するものです。分割した際に、両方のサブセットの合計が等しくなる場合、`True`を返します。これは、数字の集合が指定した合計（この場合、全体の合計の半分）を持つサブセットが存在するかどうかを調べる問題として捉えることができます。

コードの説明を部分ごとに行います。

1. ```python
   if sum(nums) % 2:
       return False
   ```

   - 先ず、`nums`の全ての要素の合計が偶数でない場合、2つの等しい合計に分割することは不可能なので`False`を返します。

2. ```python
   dp = set()
   dp.add(0)
   ```

   - `dp`という集合を初期化します。この`dp`は、現在の要素までを使用して達成できる合計の集合を表します。初期状態では、どの要素も使用しない`0`だけが存在します。

3. ```python
   target = sum(nums) // 2
   ```

   - `target`は、`nums`の全ての要素の合計の半分を表します。この値をサブセットの合計が達成する必要があります。

4. ```python
   for i in range(len(nums) - 1, -1, -1):
       nextDP = set()
       for t in dp:
           if (t + nums[i]) == target:
               return True
           nextDP.add(t + nums[i])
           nextDP.add(t)
       dp = nextDP
   ```

   - 逆順に`nums`の要素を走査します。`nextDP`は、現在の要素を考慮したときに達成できる合計の集合を一時的に保存するためのものです。
   - 現在の`dp`の各合計に現在の要素を足して新しい合計を作り、それが`target`に等しいかどうかをチェックします。等しい場合、`True`を返して処理を終了します。
   - `nextDP`には、現在の要素を加えることで新たに達成できる合計と、現在の要素を加えない場合の合計の両方を追加します。
   - 最後に、`dp`を`nextDP`で更新します。

5. ```python
   return False
   ```

   - ループが終了し、どのサブセットも`target`と等しい合計を持たない場合、`False`を返します。

このコードは、動的計画法の一種で、特に「部分和問題」として知られる問題を解くためのものです。
"""