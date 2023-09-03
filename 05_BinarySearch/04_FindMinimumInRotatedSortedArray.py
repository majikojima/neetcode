from typing import List

def findMin(nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]

nums = [3,4,5,1,2]
print(findMin(nums))

"""
この関数は、ローテート（回転）されたソート済みリストから最小の値を見つけるためのものです。ローテートされたソート済みリストとは、あるソート済みのリストが回転して、一部が前に移動したリストのことを指します。この関数は二分探索を利用して効率的にその最小値を見つけます。

大まかな説明:
- 二分探索を用いてローテートされたソート済みリストから最小値を見つける関数です。

部分毎の説明:

1. 
```python
l, r = 0, len(nums) - 1
```
リスト`nums`の最初と最後のインデックスをそれぞれ`l`と`r`に設定します。

2.
```python
while l < r:
```
`l`が`r`より小さい間、ループを継続します。

3.
```python
m = l + (r - l) // 2
```
中央のインデックス`m`を求めます。これは二分探索の基本的なステップです。

4.
```python
if nums[m] > nums[r]:
    l = m + 1
```
もし中央の値が右端の値よりも大きい場合、最小値は`m`の右側に位置していることになります。そのため、`l`を`m + 1`に更新して探索範囲を絞ります。

5.
```python
else:
    r = m
```
中央の値が右端の値よりも小さい、または等しい場合、最小値は`m`の位置、またはそれより左側に位置しています。したがって、`r`を`m`に更新して探索範囲を絞ります。

6.
```python
return nums[l]
```
ループが終了した後、`l`の位置に最小の値が存在しています。その値を返します。
"""