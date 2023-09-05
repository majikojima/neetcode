from typing import List
import heapq

class Solution2:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]

s = Solution2()

nums = [3,2,1,5,6,4]
k = 2
print(s.findKthLargest(nums, k))

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(s.findKthLargest(nums, k))

"""
このコードは、与えられたリストからk番目に大きい数字を探すためのものです。具体的には、クイックセレクトというアルゴリズムを使用しています。クイックセレクトは、クイックソートの一部としてのパーティションを利用するアルゴリズムですが、完全にソートするのではなく、特定の「k番目」の要素を効率的に探すためのものです。

それでは、コードの部分毎の説明を行います：

1. `partition`メソッド:
    - この関数は、クイックソートの核心部分であるパーティショニング処理を行います。
    - 与えられたリストの`right`番目の要素をピボットとして選びます。
    - `left`から`right-1`までの要素をループして、ピボットより小さいか等しい要素を左側に配置します。
    - 最後にピボットを正しい位置（`fill`の位置）に移動します。
    - ピボットの新しいインデックスを返します。

2. `findKthLargest`メソッド:
    - この関数はk番目に大きい数字を探しますが、kのインデックスをリストの長さから引いたものとして考えます（これにより、k番目に大きい数のインデックスが小さい方からの位置として扱えるためです）。
    - `left`と`right`を使って、リスト内で検討すべき範囲を定義します。
    - `while`ループで、ピボットの位置がkと一致するまで続けます。
        - もしピボットの位置がkより小さい場合、k番目の数は右側にあるため、`left`を更新します。
        - もしピボットの位置がkより大きい場合、k番目の数は左側にあるため、`right`を更新します。
    - インデックス`k`の要素がk番目に大きい数字であるため、これを返します。

このアルゴリズムの美しさは、全リストをソートすることなく、k番目に大きい数字をO(N)の平均時間で見つけることができる点にあります。ただし、最悪の場合の時間計算量はO(N^2)となりますが、平均的には非常に高速です。
"""