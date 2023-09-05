from typing import List

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

def result(head, k):
    s = Solution()
    llh = list_to_linkedlist(head)
    result = s.reverseKGroup(llh, k)

    current_node = result
    while current_node is not None:
        print(current_node.val)
        current_node = current_node.next
    print("")

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = groupPrev = ListNode(0, head)
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupPrev.next = kth
            groupNext = kth.next

            # reverse group
            prev, curr = groupNext, head
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            groupPrev = head
            head = groupNext
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

head = [1,2,3,4,5]
k = 2
result(head, k)

k = 3
result(head, k)

"""
このコードは、与えられたリンクリストの隣接するk個のノードを反転させるものです。リンクリストにはノードが連結しており、各ノードは値と次のノードへの参照を持っています。

コードの大まかな説明：
1. リンクリストの先頭にダミーノードを挿入して、変更を容易に行います。
2. k個のノードが存在する限り、k個のノードを反転させ続けます。
3. k個のノードを反転させる際には、そのグループの最後のノードの次のノードを参照して保存し、反転処理を行います。

部分ごとの詳細説明：

1. `dummy = groupPrev = ListNode(0, head)`
   - ダミーノードを作成して、リンクリストの先頭に配置します。このダミーノードは反転処理を簡単にするために使用されます。

2. `kth = self.getKth(groupPrev, k)`
   - 現在のノード（`groupPrev`）からk番目のノードを取得します。このメソッドは、k個のノードが存在するかを確認するためのものです。

3. `if not kth: break`
   - k番目のノードが存在しない場合、ループを終了します。

4. `groupPrev.next = kth` & `groupNext = kth.next`
   - `groupPrev`の次のノードをk番目のノードに更新し、k+1番目のノードを`groupNext`に保存します。

5. 反転処理（`# reverse group`以下の部分）：
   - k個のノードを反転させます。反転するために、各ノードの`next`プロパティを前のノードに更新します。

6. `groupPrev = head` & `head = groupNext`
   - `groupPrev`を現在のノードグループの最初のノードに更新し、`head`を次のノードグループの最初のノードに更新します。

7. `def getKth(self, curr, k):`
   - このメソッドは、与えられたノードからk番目のノードを取得するためのものです。k番目のノードが存在しない場合、このメソッドはNoneを返します。

このコードの鍵は、ポインタの操作とリンクリストの反転です。リンクリストのノードを反転させる際のポインタの操作を頭の中でイメージしながら読むと、理解が深まります。
"""

"""
このコードは、リンクリスト内の隣接するk個のノードを反転させるものです。リンクリストに慣れていないと、特にノードのポインタ操作は難しい部分があります。

`reverseKGroup`メソッドの主要な部分は、k個のノードグループを反転させる部分です。この反転の中で、特定のノードのポインタの操作を行っています。

まず、理解を助けるためのヒントをいくつか示します。

1. **リンクリストの基本理解**：
   - リンクリストはノードのチェーンです。各ノードは値を持ち、次のノードへの参照（ポインタ）を持っています。
   - リンクリストを操作する際には、これらの「次のノードへの参照」を変更することで、ノード間の接続を変えることができます。

2. **反転のメカニズムの理解**：
   - k個のノードを反転するとき、反転したノードグループの最後のノードが最初になり、最初のノードが最後になります。
   - 反転の操作は、ノード間の「次のノードへの参照」を変更することで行います。

3. **groupPrev, head, groupNextの役割の理解**：
   - `groupPrev`は現在のkノードグループの直前のノードを指します。
   - `head`は現在のkノードグループの最初のノードを指します。
   - `groupNext`は次のkノードグループの最初のノードを指します（またはリンクリストの終端の場合もあります）。

以下の部分を注目してみてください：
```python
groupPrev.next = kth
groupNext = kth.next
```
これは、`groupPrev`を次のkノードグループの最後のノード、`kth`に接続しています。そして、`groupNext`を次のkノードグループの最初のノードに更新しています。

反転処理の後、以下の部分があります：
```python
groupPrev = head
head = groupNext
```
これは、`groupPrev`を現在のkノードグループの最後（反転後は最初だった）のノード、`head`に更新して、次のkノードグループの最初のノード、`groupNext`に`head`を更新しています。

このようなポインタの操作を頭の中でイメージしながら読むと、コードの意図が理解しやすくなります。リンクリストの反転やノードの移動に関する図を描きながら考えることも、理解の助けになります。
"""

"""
1. **初期化**:
まず、ダミーのノード`dummy`を作成し、`groupPrev`として設定します。このノードは結果の先頭のノードを追跡するためのものです。

2. **ループの開始**:
`getKth`関数は、現在のノード（最初は`dummy`）から`k`ノード先のノードを返します。最初のループでは、この関数はノード`2`を返します。

3. **グループの反転**:
現在のノード（ノード`1`）から`kth`ノード（ノード`2`）までの間のノードを逆転します。この例では、ノード`1`とノード`2`が逆転され、以下のようになります。
```
dummy -> 2 -> 1 -> 3 -> 4 -> 5
```
この後、`groupPrev`はノード`1`を指し、`head`（現在のノードの先頭）はノード`3`に更新されます。

4. **次のループ**:
`getKth`関数は、ノード`4`を返します。次に、ノード`3`とノード`4`が逆転され、以下のようになります。
```
dummy -> 2 -> 1 -> 4 -> 3 -> 5
```
再び、`groupPrev`はノード`3`に更新され、`head`はノード`5`に更新されます。

5. **終了条件のチェック**:
`getKth`関数は、ノード`5`の次にノードがないため`None`を返します。これは終了条件となるため、ループは終了します。

6. **結果の返却**:
`dummy.next`（すなわちリンクドリストの先頭）が返されます。この結果は`[2, 1, 4, 3, 5]`となります。
"""