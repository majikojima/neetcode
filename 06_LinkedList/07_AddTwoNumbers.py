#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    while l1 or l2 or carry:
        if l1:
            v1 = l1.val
        else:
            v1 = 0
        if l2:
            v2 = l2.val
        else:
            v2 = 0

        # new digit
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        cur.next = ListNode(val)

        # update prts
        cur = cur.next
        if l1:
            l1 = l1.next
        else:
            l1 = None
        if l2:
            l2 = l2.next
        else:
            l2 = None

    return dummy.next

def list_to_linkedlist(nums):
    dummy = ListNode(0)
    ptr = dummy
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
    return dummy.next

def result(l1, l2):
    print(l1,l2)
    linked_list1 = list_to_linkedlist(l1)
    linked_list2 = list_to_linkedlist(l2)

    result = addTwoNumbers(linked_list1, linked_list2)

    current_node = result
    while current_node is not None:
        print(current_node.val)
        current_node = current_node.next
    print("")

l1 = [2,4,3]
l2 = [5,6,4]
result(l1,l2)

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
result(l1,l2)

"""
この関数は、2つのリンクリスト `l1` と `l2` を入力として受け取り、これらのリンクリストで表される2つの数値を加算して、その結果を新しいリンクリストとして返します。以下にこの関数の動作を詳しく説明します。

### 大まかな説明:

この関数は、2つのリンクリストを頭から順に走査して、ノードの値を1つずつ加算し、その結果を新しいリンクリストに追加します。もし、加算の結果が10を超えた場合、繰り上がりの値を次の加算に利用します。

### 部分毎の説明:

1. **初期設定**:
    ```python
    dummy = ListNode()
    cur = dummy
    carry = 0
    ```
   - `dummy` という仮のノードを作成して、最終的な結果のリストの先頭に使います。
   - `cur` は新しく作成するリンクリストの現在のノードを指すためのポインタです。
   - `carry` は繰り上がりの値を保存します。初めは0です。

2. **リンクリストの走査と加算**:
    ```python
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
    ```
    - `l1` と `l2` のどちらか、または `carry` がまだ存在する限り、ループを継続します。
    - `v1` と `v2` は、それぞれ `l1` と `l2` の現在のノードの値を取得します。存在しない場合は0を取得します。

3. **新しいノードの作成と繰り上がりの計算**:
    ```python
    val = v1 + v2 + carry
    carry = val // 10
    val = val % 10
    cur.next = ListNode(val)
    ```
    - `val` は `v1`, `v2`, そして繰り上がりの `carry` を加算した結果です。
    - 10で割った商を新しい繰り上がりの値として `carry` に保存します。
    - 10で割った余りが新しいノードの値となります。

4. **ポインタの更新**:
    ```python
    cur = cur.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
    ```
    - `cur` ポインタを次のノードに移動します。
    - `l1` と `l2` のポインタもそれぞれ次のノードに移動します（存在する場合）。

5. **結果の返却**:
    ```python
    return dummy.next
    ```
    - `dummy` の次のノードが最終的な結果のリンクリストの先頭となるので、これを返却します。

この関数を利用すると、2つのリンクリストで表される数値を効率的に加算することができます。
"""