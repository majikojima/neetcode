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

def reorderList(head: ListNode) -> None:
    # find middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse second half
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    # merge two halfs
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
    
nums = [1,2,3,4,5]
print(nums)
linked_list = list_to_linkedlist(nums)

reorderList(linked_list)

current_node = linked_list
while current_node:
    print(current_node.val)
    current_node = current_node.next

"""
このコードは、指定されたシングルリンクリストを特定の方法で並び替えるためのものです。具体的には、リストを中央で分割し、後半を逆順にしてから、前半と後半を交互に結合しています。

### 大まかな説明
1. リストを中央で2つに分割します。
2. 2つ目のリスト（後半）を逆順にします。
3. 2つのリストを交互に結合して、1つのリストを作成します。

### 部分毎の説明
1. **リストの中央を見つける**:
```python
slow, fast = head, head.next
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```
この部分では、2つのポインタ、`slow`と`fast`を使ってリストの中央を見つけています。`fast`ポインタは2つのノードを一度に移動し、`slow`ポインタは1つのノードを移動します。その結果、`fast`ポインタがリストの終わりに達したとき、`slow`ポインタはリストの中央に位置します。

2. **後半のリストを逆順にする**:
```python
second = slow.next
prev = slow.next = None
while second:
    tmp = second.next
    second.next = prev
    prev = second
    second = tmp
```
`slow`ポインタの次のノードから後半のリストが始まります。この部分では、後半のリストを逆順にしています。

3. **2つのリストを交互に結合**:
```python
first, second = head, prev
while second:
    tmp1, tmp2 = first.next, second.next
    first.next = second
    second.next = tmp1
    first, second = tmp1, tmp2
```
ここで、元のリストの前半と逆順になった後半を交互に結合しています。

以上、この`reorderList`関数は、与えられたリンクリストを中央で分割し、後半を逆順にし、前半と後半を交互に結合することで、リストを再配列しています。
"""

"""
確かに、初めて見るとこの部分は少し難解に見えますが、リンクリストの基本的な操作を理解していると、このロジックの背後にある考え方は明確になります。

まず、この部分のコードの目的は、`first`と`second`という2つのリンクリストを交互に結合することです。以下は、この処理を理解するためのステップバイステップのガイドです。

1. **初期状態**:  
    - `first`は元のリストの前半部分の先頭を指しています。
    - `second`は後半部分の逆順リストの先頭を指しています（`prev`によって逆順にされた後半部分）。

2. **交互に結合する**:
    - `tmp1`は`first`の次のノードを保持しており、`tmp2`は`second`の次のノードを保持しています。これにより、変更を行う間、これらのノードの参照を失わないようにしています。
    - `first.next = second`で、`first`の次のノードとして`second`を設定します。これにより、`first`と`second`の最初のノードが結合されます。
    - `second.next = tmp1`で、`second`の次のノードとして`first`の元々の次のノード（`tmp1`）を設定します。これで、2つのノードが交互に結合されました。
    - 最後に、`first`と`second`をそれぞれ次のノードに更新して、次のペアのノードで同じ操作を続ける準備をします。

3. **ループの終了**:  
    - `while second:`という条件のため、`second`リストが終了するとループが終了します。通常、後半部分が前半部分よりも長いか同じ長さであるため、この条件が十分です。

この結合の操作を視覚的に理解するためには、紙にリンクリストを描きながら、各ステップでどのノードがどのノードを指しているかをトレースするのが有効です。
"""

"""
了解しました。`nums = [1,2,3,4]`のリストを例に、上記のリストの結合操作をシミュレーションしてみます。

まず、前提として、このリストは前半部分`[1,2]`と後半部分`[3,4]`に分けられるとし、後半部分は逆順になっているとします。したがって、`first`は`[1,2]`を、`second`は`[4,3]`を指しているとします。

以下は各ステップでのシミュレーションです：

1. **初期状態**:
    ```
    first -> [1,2]
    second -> [4,3]
    ```

2. **1回目のループ**:
   - `tmp1 = first.next` → `tmp1`は`[2]`
   - `tmp2 = second.next` → `tmp2`は`[3]`
   - `first.next = second` → `first`の次は`second`になる
   - `second.next = tmp1` → `second`の次は`tmp1`になる
   - `first`と`second`を更新
     ```
     first -> [2]
     second -> [3]
     ```

   現在の結果：`[1,4,2,3]`

3. **2回目のループ**:
   - `tmp1 = first.next` → `tmp1`はなし（`first`の次のノードが存在しない）
   - `tmp2 = second.next` → `tmp2`もなし
   - `first.next = second` → `first`の次は`second`になる
   - `second.next = tmp1` → `second`の次は`tmp1`になるが、`tmp1`は存在しないので変更はなし
   - `first`と`second`を更新するが、`second`が存在しないためループ終了

   現在の結果：`[1,4,2,3]`（変更なし）

以上の操作を完了すると、元のリスト`[1,2,3,4]`は`[1,4,2,3]`に変わります。
"""

"""
`nums = [1,2,3,4,5]`のリストを例にして、再度シミュレーションしてみます。ただし、こちらのシミュレーションはリストノードの結合操作に基づいています。したがって、前提として、このリストは前半部分`[1,2,3]`と後半部分`[4,5]`に分けられるとし、後半部分は逆順になっているとします。したがって、`first`は`[1,2,3]`を、`second`は`[5,4]`を指しているとします。

以下は各ステップでのシミュレーションです：

1. **初期状態**:
    ```
    first -> [1,2,3]
    second -> [5,4]
    ```

2. **1回目のループ**:
   - `tmp1 = first.next` → `tmp1`は`[2,3]`
   - `tmp2 = second.next` → `tmp2`は`[4]`
   - `first.next = second` → `first`の次は`second`になる
   - `second.next = tmp1` → `second`の次は`tmp1`になる
   - `first`と`second`を更新
     ```
     first -> [2,3]
     second -> [4]
     ```

   現在の結果：`[1,5,2,3,4]`

3. **2回目のループ**:
   - `tmp1 = first.next` → `tmp1`は`[3]`
   - `tmp2 = second.next` → `tmp2`はなし（`second`の次のノードが存在しない）
   - `first.next = second` → `first`の次は`second`になる
   - `second.next = tmp1` → `second`の次は`tmp1`になる
   - `first`と`second`を更新
     ```
     first -> [3]
     second -> None
     ```

   現在の結果：`[1,5,2,4,3]`

以上の操作を完了すると、元のリスト`[1,2,3,4,5]`は`[1,5,2,4,3]`に変わります。
"""