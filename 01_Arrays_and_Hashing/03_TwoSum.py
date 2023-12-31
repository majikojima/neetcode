# [https://leetcode.com/problems/two-sum/]

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            print(prevMap)
            print(i, n)
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

s = Solution()

nums = [2,7,11,15]
target = 9

result = s.twoSum(nums, target)
print(result)

"""
もちろんです。このコードは、リスト内の2つの数字の合計が特定の目標値と等しくなるような2つの数字のインデックスを見つけるためのものです。

以下、各行の説明です：

```python
class Solution:
```
新しいクラス`Solution`を定義します。このクラスは、他のプログラムや関数から再利用しやすいように特定の機能をまとめたものです。

```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
```
`twoSum`というメソッドを定義します。このメソッドは、整数のリスト`nums`と目標値`target`を引数に取ります。戻り値は、2つの整数のインデックスのリストです。

```python
        prevMap = {}  # val -> index
```
空の辞書`prevMap`を作成します。この辞書は、値をキーとしてそのインデックスを値として保存します。

```python
        for i, n in enumerate(nums):
```
`enumerate`関数を使用して、リスト`nums`を反復処理します。`i`は現在の要素のインデックスを、`n`はその値を表します。

```python
            diff = target - n
```
目標値`target`から現在の値`n`を引き、その差`diff`を計算します。この`diff`が以前の要素の中に存在する場合、`n`と`diff`の和は`target`と等しくなります。

```python
            if diff in prevMap:
```
もし`diff`が`prevMap`の中のキー（つまり、以前に見た数値）である場合、`n`と`diff`の和が`target`と等しいという条件が満たされます。

```python
                return [prevMap[diff], i]
```
その場合、`diff`のインデックス（`prevMap[diff]`）と現在のインデックス`i`をリストとして返します。これが解答となります。

```python
            prevMap[n] = i
```
`diff`が`prevMap`に存在しない場合、現在の要素`n`とそのインデックス`i`を`prevMap`に追加します。これにより、次に`diff`を見つけたときに、その位置を速やかに参照できるようになります。
"""

"""
この問題は、リスト`nums`内の2つの数値の和が特定の`target`と等しくなる2つの数値のインデックスを見つけることです。解決策はハッシュマップ（Pythonでは辞書と呼ばれます）を使用し、リストを通過するたびに各要素をハッシュマップに追加していきます。

関数`twoSum`の初めての行では、空のハッシュマップ`prevMap`を作成します。ここではキーとしてリスト`nums`内の値、値としてそのインデックスを保持します。このマップは、リストを最初から最後まで一度だけスキャンすることで解を見つけるために使用します。

初めての段階では`prevMap`は空です。それは、まだリストのいずれの要素も見ていないからです。`nums`リストを左から右へと進むにつれて、`prevMap`は更新され、各要素とそのインデックスが追加されます。

`prevMap`は次のように使用されます：各ステップで、現在の要素`n`と`target`の差`diff`を計算し、`diff`が`prevMap`に存在するかどうかを確認します。`diff`が`prevMap`に存在する場合、それは`diff`と`n`の和が`target`に等しいということを意味します。このとき、`diff`のインデックスと現在のインデックス`i`を返すことで、問題の解答が得られます。なお、このコードは各要素を一度だけ確認するため、時間複雑度はO(n)となります。
"""