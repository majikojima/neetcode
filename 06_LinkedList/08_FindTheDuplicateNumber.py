from typing import List
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findDuplicate(nums: List) -> int:
    # cycle detection
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # identifying cycle start points (duplicate numbers)
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

nums = [1,3,4,2,2]
print(findDuplicate(nums))

"""
この関数は、与えられた整数のリスト `nums` 内で重複する要素（値）を見つけて返すためのものです。この問題は、重複を探すのに特別な方法（二重ポインタやサイクル検出アルゴリズム）を用いています。

### 大まかな説明:

このアルゴリズムは、リンクリストのサイクル検出の技法を用いています。具体的には、リスト内の各要素をノード、各要素の値を次のノードへのポインタとして扱います。この方法を用いると、重複する数字が存在する場合、必ずサイクルが形成されることになります。このアルゴリズムは、まずサイクルを検出し、次にサイクルの開始地点を特定することで、重複する数字を見つけ出します。

### 部分毎の説明:

1. **サイクル検出**:
    ```python
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    ```
    - `slow` と `fast` は二重ポインタとして機能し、それぞれ1つと2つずつ移動します。
    - サイクルが存在する場合、`fast` ポインタは最終的に `slow` ポインタと同じ位置になるという性質を利用しています。

2. **サイクルの開始地点（重複数字）の特定**:
    ```python
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow
    ```
    - `slow` ポインタをサイクルの検出時の位置に保持し、新たな `slow2` ポインタをリストの先頭から移動させます。
    - 両方のポインタが同じ位置になった場合、それはサイクルの開始地点、すなわち重複する数字の位置であると判断できます。

このアルゴリズムの美しさは、追加のデータ構造を使用せずにO(1)の空間計算量で重複する数字を検出できる点にあります。
"""

"""
確かに、ある種の`nums`に対してはこのアルゴリズムがうまく機能しないことがあります。しかし、この関数は特定の前提条件の下で正しく動作するように設計されています。

このアルゴリズムの正当性を理解するための主な前提条件は以下の通りです：

1. `nums`の要素は1から`len(nums) - 1`までの整数です。これにより、`nums`の各要素が有効なインデックスを指すことが保証されます。
2. `nums`にはちょうど1つの重複した数字が含まれていること。このため、サイクルが必ず存在することが保証されます。

これらの前提条件が満たされている場合、アルゴリズムは正しく動作します。それに対して、これらの条件が満たされていない場合、たとえば`nums`が`[3,5,6,7]`のようなリストの場合、このアルゴリズムは正しく動作しません。

したがって、この関数を使用する前に、上記の前提条件が満たされているかどうかを確認することが非常に重要です。
"""