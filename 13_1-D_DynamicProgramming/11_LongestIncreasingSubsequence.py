from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    LIS = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))

nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))

nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))

"""
このコードは、与えられた整数のリスト`nums`の中で最も長い増加部分列（Longest Increasing Subsequence、LIS）の長さを返す問題の解法です。

全体の流れ：
`nums`の各要素について、それをLISの最初の要素として考慮し、その後に続く可能性のある要素をチェックして、最も長いLISを探索します。

以下は各部分の詳細な説明です：

1. `LIS = [1] * len(nums)`:
   - `nums`の各要素に対応するLISの長さを記録するリストを初期化します。最初は各要素自体が長さ1の部分列であると仮定しているので、すべての値が1で初期化されます。

2. `for i in range(len(nums) - 1, -1, -1):`:
   - `nums`の要素を後ろから前に向かってループします。`i`は現在の要素のインデックスです。

3. `for j in range(i + 1, len(nums)):`:
   - `i`よりも後ろにある要素を探索するループです。`j`は次の要素のインデックスです。

4. `if nums[i] < nums[j]:`:
   - 現在の要素`nums[i]`が次の要素`nums[j]`よりも小さい場合（増加している場合）、以下のコードを実行します。

5. `LIS[i] = max(LIS[i], 1 + LIS[j])`:
   - 現在の要素`nums[i]`から始めるLISの長さを更新します。`1 + LIS[j]`は、現在の要素を`nums[j]`の前に追加した場合のLISの長さを示しています。

6. `return max(LIS)`:
   - 最も長いLISの長さを返します。`LIS`リストの中の最大値が、与えられたリスト`nums`の中で最も長い増加部分列の長さになります。

要約すると、このコードは動的プログラミングを使用して、与えられたリスト`nums`内で最も長い増加部分列の長さを効率的に計算します。
"""

"""
指定された`nums = [0,1,0,3,2,3]`での`lengthOfLIS`関数のシミュレーションを行います。

初めに、
```python
LIS = [1, 1, 1, 1, 1, 1]
```
として、`nums`の各要素に対応するLISの長さを記録するリスト`LIS`を初期化します。

シミュレーションを開始します。

1. i = 5 (`nums[5] = 3`)
    - j = 6: ループの外なのでスキップ
    - LIS = [1, 1, 1, 1, 1, 1]

2. i = 4 (`nums[4] = 2`)
    - j = 5 (`nums[5] = 3`): nums[i] < nums[j] なので、LIS[4] = max(1, 1 + LIS[5]) = 2
    - j = 6: ループの外なのでスキップ
    - LIS = [1, 1, 1, 1, 2, 1]

3. i = 3 (`nums[3] = 3`)
    - j = 4: nums[i] > nums[j] なのでスキップ
    - j = 5: nums[i] = nums[j] なのでスキップ
    - j = 6: ループの外なのでスキップ
    - LIS = [1, 1, 1, 1, 2, 1]

4. i = 2 (`nums[2] = 0`)
    - j = 3 (`nums[3] = 3`): nums[i] < nums[j] なので、LIS[2] = max(1, 1 + LIS[3]) = 2
    - j = 4 (`nums[4] = 2`): nums[i] < nums[j] なので、LIS[2] = max(2, 1 + LIS[4]) = 3
    - j = 5 (`nums[5] = 3`): nums[i] < nums[j] なので、LIS[2] = max(3, 1 + LIS[5]) = 3
    - j = 6: ループの外なのでスキップ
    - LIS = [1, 1, 3, 1, 2, 1]

5. i = 1 (`nums[1] = 1`)
    - j = 2: nums[i] > nums[j] なのでスキップ
    - j = 3 (`nums[3] = 3`): nums[i] < nums[j] なので、LIS[1] = max(1, 1 + LIS[3]) = 2
    - j = 4 (`nums[4] = 2`): nums[i] < nums[j] なので、LIS[1] = max(2, 1 + LIS[4]) = 3
    - j = 5 (`nums[5] = 3`): nums[i] < nums[j] なので、LIS[1] = max(3, 1 + LIS[5]) = 3
    - j = 6: ループの外なのでスキップ
    - LIS = [1, 3, 3, 1, 2, 1]

6. i = 0 (`nums[0] = 0`)
    - j = 1 (`nums[1] = 1`): nums[i] < nums[j] なので、LIS[0] = max(1, 1 + LIS[1]) = 4
    - j = 2: nums[i] = nums[j] なのでスキップ
    - j = 3 (`nums[3] = 3`): nums[i] < nums[j] なので、LIS[0] = max(4, 1 + LIS[3]) = 4
    - j = 4 (`nums[4] = 2`): nums[i] < nums[j] なので、LIS[0] = max(4, 1 + LIS[4]) = 4
    - j = 5 (`nums[5] = 3`): nums[i] < nums[j] なので、LIS[0] = max(4, 1 + LIS[5]) = 4
    - j = 6: ループの外なのでスキップ
    - LIS = [4, 3, 3, 1, 2, 1]

最後に`return max(LIS)`として、LISの中で最も大きな値（この場合、4）を返します。
"""