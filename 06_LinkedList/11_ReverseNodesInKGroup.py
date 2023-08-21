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

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        # reverse group
        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    return dummy.next

def getKth(curr: ListNode, k: int) -> ListNode:
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

head = [1,2,3,4,5]
k = 2
llh = list_to_linkedlist(head)

result = reverseKGroup(llh, k)

current_node = result
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next

"""
このコードは、リンクドリストで与えられたノードのグループを逆順にすることを目的としています。具体的には、`k`のサイズごとのノードのグループを逆順にします。

### 大まかな説明：
- 入力としてリンクドリストのヘッドと整数`k`を受け取ります。
- リスト内の各`k`サイズのグループを逆順にします。
- すべてのグループが逆順になった後、新しいリンクドリストのヘッドを返します。

### 部分毎の説明：

1. `dummy = ListNode(0, head)`: 
   - ダミーノードを作成して、元のリンクドリストの前に配置します。このノードは、逆順操作中にヘッドが変わる可能性があるので、結果を簡単に返すために役立ちます。

2. `groupPrev = dummy`:
   - 現在のグループの前のノードを指し示すポインタとして`groupPrev`を使用します。

3. `while True:`:
   - 各グループを逆順にする操作を繰り返します。

4. `kth = self.getKth(groupPrev, k)`:
   - 現在のグループの最後のノードを見つけるためのヘルパー関数を呼び出します。

5. `if not kth:`:
   - `k`サイズのグループがもうない場合、ループを終了します。

6. `groupNext = kth.next`:
   - 現在のグループの次のグループの先頭ノードを保存します。

7. `# reverse group` と以下の部分:
   - 現在の`k`サイズのグループを逆順にします。この逆順の処理は、ポインタの入れ替えを使って行います。

8. `tmp = groupPrev.next` ... `groupPrev = tmp`:
   - 次のグループの逆順のために、`groupPrev`を適切な位置に移動します。

9. `return dummy.next`:
   - 新しいリンクドリストのヘッドを返します。ダミーノードの次のノードが新しいヘッドとなります。

10. `def getKth(self, curr, k):`:
   - 与えられたノードから数えて`k`番目のノードを返すヘルパー関数です。もし`k`番目のノードが存在しない場合、`None`を返します。
"""

"""
コード内の`groupPrev`と`groupNext`の変数は、リンクドリストの一部（k個のノード）を逆転させるときに、逆転されるグループの前後のノードとの関係を保持・管理するために存在しています。

具体的には：

1. **`groupPrev`**:
    - これは逆転されるグループの「前」のノードを指します。具体的には、逆転されるグループの最初のノードの1つ前のノードを指しています。
    - 逆転操作が行われると、元の逆転グループの最後のノードが新しいグループの最初のノードになるため、`groupPrev`の`next`ポインタはこの新しいグループの最初のノード（すなわち`kth`）に更新されます。
    - 次の逆転操作のために、`groupPrev`は逆転されたグループの最後のノードを指すように更新されます。

2. **`groupNext`**:
    - これは逆転されるグループの「後」のノードを指します。具体的には、逆転されるグループの最後のノードの1つ後のノードを指します。
    - `groupNext`は逆転操作自体に直接影響を与えるわけではありませんが、現在の逆転グループのノードの逆転操作を行う際の終了条件として使用されます。`curr`が`groupNext`に到達したら、逆転操作は終了する、というわけです。

これらの変数が存在する理由は、リンクドリストの中の一部のノードだけを逆転させる操作を行う際に、逆転部分の前後のリンクドリストとの関連性・連続性を保つためです。この2つの変数によって、リンクドリスト全体が連続的なデータ構造として保持され、断裂や失われる部分がないようになっています。
"""

"""
はい、この部分はリンクドリストの逆転操作の一部としてのポインタの入れ替えを行っていますが、この3行のコードを分解して詳しく説明してみましょう。

考えるポイントとして、`groupPrev`は現在の逆転グループの前にあるノードを指しています。そして、`kth`は逆転グループの最後のノードを指しています。逆転操作を行うと、`kth`は新しいグループの先頭になります。

1. `tmp = groupPrev.next`: 
    - `tmp`には、逆転する前のグループの先頭ノードが保存されます。このノードは逆転した後、グループの最後のノードになります。

2. `groupPrev.next = kth`: 
    - ここでは、前のグループ（またはダミーノード）の`next`ポインタを、逆転グループの新しい先頭（`kth`）に接続しています。

3. `groupPrev = tmp`: 
    - 最後に、`groupPrev`を逆転したグループの最後のノード（`tmp`、つまり逆転する前のグループの先頭）に移動します。次の逆転グループのための準備として、このノードを起点にして次のグループを逆転します。

この3行のコードは、リンクドリストを逆転させる際のポインタのつなぎかえを行う部分で、アルゴリズム全体の中で非常に重要な役割を果たしています。
"""

"""
与えられたコードを使用して、`head = [1,2,3,4,5]` と `k = 2` での動作をシミュレートして説明します。まず、簡易的なリンクドリストの実装が必要です。

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

初めに、このリンクドリストを構築します。

```
head -> 1 -> 2 -> 3 -> 4 -> 5
```

`reverseKGroup` 関数を呼び出してシミュレーションを開始します。

1. 初期化:
```
dummy -> 1 -> 2 -> 3 -> 4 -> 5
groupPrev = dummy
```

2. 1回目のループ:
`getKth` 関数は、groupPrevから2ノード先、すなわちノード`2`を返します。
```
kth = 2
groupNext = 2.next = 3
```
このグループはノード`1`とノード`2`を逆転させます。
```
while curr != groupNext:
```
によって、ノード`1`とノード`2`が逆転され、
```
dummy -> 2 -> 1 -> 3 -> 4 -> 5
```
となります。

さらに、
```
tmp = groupPrev.next
groupPrev.next = kth
groupPrev = tmp
```
を更新すると、`groupPrev`はノード`1`を指すようになります。

3. 2回目のループ:
再び、`getKth` 関数が呼び出され、ノード`4`を返します。
```
kth = 4
groupNext = 4.next = 5
```
このグループはノード`3`とノード`4`を逆転させます。結果は:
```
dummy -> 2 -> 1 -> 4 -> 3 -> 5
```

同様に、`groupPrev`をノード`3`に更新します。

4. 3回目のループ:
`getKth`関数はノード`5`の次はないため`None`を返します。したがって、ループは終了します。

最終的なリンクドリスト:
```
dummy -> 2 -> 1 -> 4 -> 3 -> 5
```

したがって、結果として、`[2,1,4,3,5]`が得られます。
"""