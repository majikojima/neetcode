from typing import List

def rob(nums: List[int]) -> int:
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

def helper(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

nums = [2,3,2]
print(rob(nums))

nums = [1,2,3,1]
print(rob(nums))

nums = [1,2,3]
print(rob(nums))

"""
このコードは「House Robber II」の問題を解決するものです。基本的な「House Robber」の問題と似ていますが、1つの重要な違いがあります。すなわち、家が円環状に並んでおり、最初の家と最後の家は隣接しているという点です。したがって、最初の家を盗む場合、最後の家は盗むことができません。この制約を考慮するために、上記のコードは3つのケースを考慮しています。

**大まかな説明**:
このアルゴリズムは、次の3つのケースの最大の利益を取得し、最大値を返します。
1. 最初の家のみを盗む。
2. 最初の家を除外して、2番目の家から最後の家までを考慮する。
3. 最後の家を除外して、最初の家から最後の前の家までを考慮する。

**部分毎の説明**:

1. `def rob(self, nums: List[int]) -> int`:
   - メイン関数です。3つのケースのうち、最大のものを返します。
   
2. `return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))`:
   - 最初の家だけを盗むケース：`nums[0]`
   - 最初の家を除いて残りを考慮するケース：`self.helper(nums[1:])`
   - 最後の家を除いて残りを考慮するケース：`self.helper(nums[:-1])`
   これらの3つのケースの最大のものを返します。
   
3. `def helper(self, nums):`:
   - 補助関数です。基本的な「House Robber」の問題の解を提供します。
   
4. `rob1, rob2 = 0, 0`:
   - `rob1`と`rob2`は、それぞれ1つ前と2つ前の家を盗んだ際の最大の利益を保持します。
   
5. `for n in nums:`:
   - 各家（`nums`の各要素）についてループを回します。
   
6. `newRob = max(rob1 + n, rob2)`:
   - 現在の家を盗む場合（`rob1 + n`）と盗まない場合（`rob2`）のうち、どちらがより多くの利益をもたらすかを評価します。
   
7. `rob1 = rob2` と `rob2 = newRob`:
   - 最新の最大の利益の情報を更新します。
   
8. `return rob2`:
   - 全ての家を考慮した後、`rob2`は最大の利益を持っているので、それを返します。

このコードは、円環状の家の配列に対して最大の盗む利益を効果的に計算する方法を提供しています。
"""