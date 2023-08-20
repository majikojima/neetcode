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
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    # delete
    left.next = left.next.next
    return dummy.next
    
nums = [1,2,3,4,5]
n = 2
linked_list = list_to_linkedlist(nums)

result = removeNthFromEnd(linked_list, n)

current_node = result
while current_node:
    print(current_node.val)
    current_node = current_node.next

"""
この関数は、シングルリンクリストから後ろからn番目のノードを削除するためのものです。リンクリストの一般的な問題で、2つのポインタ技法を使っています。

### 大まかな説明:
この関数は、1つのパスでシングルリンクリストから後ろからn番目のノードを削除します。まず、2つのポインターを定義して、2つのポインター間のギャップをnにする。次に、2つのポインターを一緒に移動して、2番目のポインターがリストの終端に達したら、最初のポインターが削除すべきノードの1つ前のノードを指すようにします。最後に、そのノードをスキップして次のノードにリンクを張り替えることで、ノードを削除します。

### 部分毎の説明:

1. **初期設定**:
    ```python
    dummy = ListNode(0, head)
    left = dummy
    right = head
    ```
    `dummy`ノードは、新しいヘッドを保持するためのダミーノードです。これは、実際のヘッドノードが削除される場合にもリストを維持できるようにするためのものです。
    `left`は`dummy`ノードを指し、`right`は実際のヘッドノードを指します。

2. **`right`ポインタをnステップ前進させる**:
    ```python
    while n > 0:
        right = right.next
        n -= 1
    ```
    このループにより、`right`ポインタは`n`ノードだけ前進します。

3. **2つのポインタを同時に移動**:
    ```python
    while right:
        left = left.next
        right = right.next
    ```
    このループは、`right`がリンクリストの終端に到達するまで、2つのポインタを一緒に移動します。この時、`left`は後ろからn+1番目のノードを指します。

4. **ノードの削除**:
    ```python
    left.next = left.next.next
    ```
    ここで、`left`ポインタの次のノードが後ろからn番目のノードなので、そのノードをスキップして次のノードにリンクします。

5. **結果の返却**:
    ```python
    return dummy.next
    ```
    最終的に、`dummy`ノードの次のノード（実際のリストのヘッドノード）を返します。
"""

"""
この関数は、リンクリストから末尾から数えてn番目のノードを削除するものです。ここでは、リンクリストとして`[1,2,3,4,5]`とn=2として例示します。

シミュレーションを行うと、以下のような手順で処理が進みます：

1. **初期化**:
    - リストのダミーノードを作成します。
    - `left` ポインタはダミーノードを指しています。
    - `right` ポインタはリンクリストの先頭を指しています。

    ```python
    dummy = ListNode(0, head)
    left = dummy
    right = head
    ```

2. **rightポインタをnステップ先に移動**:
    - `right` ポインタをnステップ先に進めます。これにより、`left` と `right` の間の距離が n + 1 となります。

    ```python
    while n > 0:
        right = right.next
        n -= 1
    ```

    この例では n=2 なので、`right` は `1` から `3` に移動します。

3. **rightがリンクリストの末尾に達するまで、leftとrightを一緒に移動**:
    - `right`がリンクリストの末尾に達するまで、`left`と`right`を同時に1ステップずつ進めます。

    ```python
    while right:
        left = left.next
        right = right.next
    ```

    これが完了すると、`left` は削除するノードの1つ前を指しています。

4. **ノードの削除**:
    - `left.next` を `left.next.next` に更新して、`n`番目のノードをリンクリストから削除します。

    ```python
    left.next = left.next.next
    ```

    この例では、ノード`4`が削除され、リンクリストは `[1,2,3,5]` となります。

5. **結果の返却**:
    - ダミーノードの次のノード、すなわちリンクリストの先頭を返します。

    ```python
    return dummy.next
    ```

    この例では、結果としてリンクリスト `[1,2,3,5]` が返されます。
"""