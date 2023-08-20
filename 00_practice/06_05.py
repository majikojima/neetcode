#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(nums):
    dummy = ListNode(0)
    ptr = dummy
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
    return dummy.next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    dummy = ListNode(0)
    dummy.next = prev
    curr = dummy
    for i in range(n - 1):
        curr = curr.next
    curr.next = curr.next.next

    prev = None
    curr = dummy.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev
    
nums = [1,2,3,4,5]
n = 2
linked_list = list_to_linkedlist(nums)

result = removeNthFromEnd(linked_list, n)

current_node = result
while current_node:
    print(current_node.val)
    current_node = current_node.next

"""
この関数は、与えられた単方向連結リスト（リンクリスト）から、末尾から数えてn番目のノードを削除するものです。このタスクは、リンクリストを2回逆転させるというアイディアに基づいて実現されています。

具体的な手順は以下の通りです：

1. **リンクリストの逆転**:
    - 最初に、リンクリストを逆転させます。
    ```python
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    ```

2. **n番目のノードの削除**:
    - リンクリストが逆転した後、先頭から数えてn番目のノードをスキップします。このために、ダミーノードを使用して、削除するノードの前のノードにアクセスできるようにします。
    ```python
    dummy = ListNode(0)
    dummy.next = prev
    curr = dummy
    for i in range(n - 1):
        curr = curr.next
    curr.next = curr.next.next
    ```

3. **リンクリストを元の順序に戻す**:
    - 最後に、リンクリストを再び逆転させて、元の順序に戻します。
    ```python
    prev = None
    curr = dummy.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    ```

4. **結果の返却**:
    - 逆転を2回行った結果、リンクリストの順序が元に戻るとともに、指定されたn番目のノードが削除された状態でリンクリストが返されます。
    ```python
    return prev
    ```

このアプローチの時間計算量はO(N)ですが、リンクリストを2回通過する必要があるため、実際の操作数は2倍になる点に注意が必要です。
"""