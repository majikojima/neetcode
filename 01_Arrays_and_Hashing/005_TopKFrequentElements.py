from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            print("count: ", count)

        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
            print("freq", freq)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            print(f"i: {i}")
            for n in freq[i]:
                print(f"n: {n}")
                res.append(n)
                print(f"res: {res}")
                if len(res) == k:
                    return res

        return res
    
s = Solution()
nums = [1,1,1,1,1,2,2,3,3,3,4,5]
k=2
result = s.topKFrequent(nums, k)

print(result)

"""
count:  {1: 1}
count:  {1: 2}
count:  {1: 3}
count:  {1: 4}
count:  {1: 5}
count:  {1: 5, 2: 1}
count:  {1: 5, 2: 2}
count:  {1: 5, 2: 2, 3: 1}
count:  {1: 5, 2: 2, 3: 2}
count:  {1: 5, 2: 2, 3: 3}
count:  {1: 5, 2: 2, 3: 3, 4: 1}
count:  {1: 5, 2: 2, 3: 3, 4: 1, 5: 1}
freq [[], [], [], [], [], [1], [], [], [], [], [], [], []]
freq [[], [], [2], [], [], [1], [], [], [], [], [], [], []]
freq [[], [], [2], [3], [], [1], [], [], [], [], [], [], []]
freq [[], [4], [2], [3], [], [1], [], [], [], [], [], [], []]
freq [[], [4, 5], [2], [3], [], [1], [], [], [], [], [], [], []]
i: 12
i: 11
i: 10
i: 9
i: 8
i: 7
i: 6
i: 5
n: 1
res: [1]
i: 4
i: 3
n: 3
res: [1, 3]
[1, 3]
"""

"""
了解しました。コードの大きなブロックごとに説明します。

1. **初期設定**:
   ```python
   count = {}
   freq = [[] for i in range(len(nums) + 1)]
   ```
   `count` という辞書は、各数値の出現頻度を数えるためのものです。`freq` は、特定の頻度での数値を格納するためのリストです。例えば、3回出現した数値は `freq[3]` に格納されます。

2. **数値の出現頻度をカウント**:
   ```python
   for n in nums:
       count[n] = 1 + count.get(n, 0)
   ```
   `nums` の中の各数値の出現頻度をカウントします。`count.get(n, 0)` は `n` が辞書に存在しない場合は0を、存在する場合はその値を取得します。

3. **頻度ごとに数値を格納**:
   ```python
   for n, c in count.items():
       freq[c].append(n)
   ```
   先ほど計算した出現頻度ごとに、該当する数値を `freq` に格納しています。

4. **上位 k の頻繁な要素を取得**:
   ```python
   res = []
   for i in range(len(freq) - 1, 0, -1):
       for n in freq[i]:
           res.append(n)
           if len(res) == k:
               return res
   ```
   最も頻度が高い要素から探していき、`k` 個の要素を `res` リストに追加します。`res` のサイズが `k` に達した時点で、結果を返します。

このアルゴリズムの中心的な考え方は、数値の出現頻度をカウントし、その頻度をインデックスとして使用して、頻度ごとに数値を整理することです。最後に、最も頻繁に出現する数値を取得するために、高い頻度から低い頻度へと進めていきます。
"""

"""
このアルゴリズムは、与えられたリスト `nums` の中から最も頻繁に出現する `k` 個の要素を返すものです。以下、各行を説明していきます。

```python
class Solution:
```
- この行は新しいクラス `Solution` を定義しています。

```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
```
- `topKFrequent` というメソッドを定義しています。このメソッドは2つの引数を受け取ります：`nums`（整数のリスト）と`k`（探している頻繁な要素の数）。

```python
count = {}
```
- 空の辞書 `count` を初期化しています。この辞書は、各数字の出現回数を格納するために使用されます。

```python
freq = [[] for i in range(len(nums) + 1)]
```
- 頻度に基づいて数字をグループ化するためのリスト `freq` を初期化しています。このリストの各要素は、その頻度の数字を格納するための空のリストです。

```python
for n in nums:
```
- `nums` の中の各数字 `n` に対してループを開始します。

```python
count[n] = 1 + count.get(n, 0)
```
- `count` 辞書を更新して、数字 `n` の出現回数をカウントします。

```python
for n, c in count.items():
```
- `count` 辞書の各キー（数字）と値（出現回数）に対してループを開始します。

```python
freq[c].append(n)
```
- 出現回数 `c` をインデックスとして使用し、`freq` リストの対応する部分に数字 `n` を追加します。

```python
res = []
```
- 結果を格納するための空のリスト `res` を初期化しています。

```python
for i in range(len(freq) - 1, 0, -1):
```
- 最も高い頻度から最も低い頻度までの逆順でループを開始します。

```python
for n in freq[i]:
```
- 特定の頻度 `i` に関連するすべての数字 `n` に対してループを開始します。

```python
res.append(n)
```
- 結果のリスト `res` に数字 `n` を追加します。

```python
if len(res) == k:
```
- `res` の長さが目的の `k` と等しいかどうかをチェックします。

```python
return res
```
- `k` 個の頻繁な要素が `res` に追加されたら、`res` を返します。

```python
# O(n)
```
- このアルゴリズムの時間複雑度が O(n) であることを示すコメントです。
"""