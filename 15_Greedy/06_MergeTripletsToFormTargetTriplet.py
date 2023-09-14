from typing import List

def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
    good = set()

    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue
        for i, v in enumerate(t):
            if v == target[i]:
                good.add(i)
    return len(good) == 3

triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]
print(mergeTriplets(triplets, target))

triplets = [[3,4,5],[4,5,6]]
target = [3,2,5]
print(mergeTriplets(triplets, target))

"""
まず、大まかな説明から始めましょう。

## 大まかな説明:
この関数は、与えられたトリプレット（3つの整数から成るリスト）の集合から、特定のターゲットトリプレットを形成できるかどうかを判断します。具体的には、複数のトリプレットを組み合わせて、ターゲットトリプレットの各要素を得られる場合にTrueを返します。それが不可能であればFalseを返します。

## 部分毎の説明:

1. `good = set()`
    - このセットは、ターゲットトリプレットの各要素を形成できるかどうかの情報を保存します。

2. `for t in triplets:`
    - 与えられたトリプレットのリストをイテレートします。

3. `if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:`
    - 現在のトリプレットの要素がターゲットの要素よりも大きいかどうかをチェックします。もしそうであれば、このトリプレットは目的のターゲットの形成に役立たないので、次のトリプレットに進むために`continue`でループをスキップします。

4. `for i, v in enumerate(t):`
    - 現在のトリプレットの各要素をインデックスと共にイテレートします。

5. `if v == target[i]:`
    - 現在の要素がターゲットの同じインデックスの要素と等しいかどうかをチェックします。

6. `good.add(i)`
    - 現在の要素がターゲットと一致した場合、そのインデックスを`good`セットに追加します。これにより、その位置の要素がターゲットトリプレットを形成するために使用できることを示しています。

7. `return len(good) == 3`
    - 最後に、`good`セットのサイズが3（つまり、3つの要素すべてがターゲットトリプレットを形成するのに適している）である場合にTrueを返し、そうでなければFalseを返します。
"""