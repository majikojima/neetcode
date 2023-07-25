#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

def list_to_linkedlist(nums):
    dummy = ListNode(0)
    ptr = dummy
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
    return dummy.next

def create_cycle_in_linkedlist(nums, pos):
    # First, create a linked list.
    head = list_to_linkedlist(nums)
    
    # If pos is -1, there is no cycle.
    if pos == -1:
        return head
    
    # Find the node where the cycle should start.
    cycle_start = head
    for _ in range(pos):
        cycle_start = cycle_start.next

    # Find the last node of the list.
    last_node = head
    while last_node.next:
        last_node = last_node.next

    # Create the cycle by setting the next of last_node as cycle_start.
    last_node.next = cycle_start

    return head


# Using your Solution class...
s = Solution()

nums = [3,4,0,-4]
pos = 1
print(nums, pos)
linked_list_with_cycle = create_cycle_in_linkedlist(nums, pos)

result = s.hasCycle(linked_list_with_cycle)

print(result)

"""
このコードは、リンクリストにサイクル（つまりループまたは円環状の構造）が存在するかどうかを判断するためのものです。ここでは、ヘアとトータスアルゴリズムまたは2つのポインター法と呼ばれる技巧を使用しています。このアルゴリズムでは、2つのポインター（この場合は`slow`と`fast`）がリンクリストを異なる速度で移動します。以下に、各行の詳細な説明を示します：

1. `slow, fast = head, head`: 最初に、2つのポインター（`slow`と`fast`）をリンクリストの先頭（`head`）に配置します。

2. `while fast and fast.next:`: `fast`と`fast.next`の両方がNone（リストの終わりまたはリストが存在しない）でない限り、このループは続きます。

3. `slow = slow.next`: `slow`ポインターを1つだけ進めます（1つのステップを移動）。

4. `fast = fast.next.next`: `fast`ポインターを2つ進めます（2つのステップを移動）。したがって、`fast`ポインターは`slow`ポインターよりも早く進みます。

5. `if slow == fast:`: `slow`ポインターと`fast`ポインターが同じノードを指している場合、リンクリストにはサイクルが存在すると判断します。これは、`fast`ポインターが`slow`ポインターを"追い越す"という事実から導かれます。これはリンクリストがサイクルを持っていて、`fast`ポインターがそのサイクルを1周またはそれ以上回った結果だけが可能です。

6. `return True`: サイクルが見つかった場合、関数は`True`を返します。

7. `return False`: ループが終了し（つまり`fast`または`fast.next`がNoneに達する）、サイクルが見つからなかった場合、関数は`False`を返します。これはリンクリストがサイクルを持っていないことを示します。

このアルゴリズムは効率的であり、リンクリスト内のすべてのノードを訪れるだけでサイクルを検出できます。
"""

"""
このアルゴリズム（ヘアとトータス、または二重ポインター法）は、特にリンクリストのサイクルを見つける問題に対して効率的であり、さまざまな問題解決のために使用されます。 

具体的には、このアルゴリズムは以下のようなシチュエーションで使用されます：

1. **リンクリスト内のサイクルを検出する**：サイクル（ループまたは環状構造）が存在する場合、`fast`ポインターは最終的に`slow`ポインターに追いつきます。この原理を使用して、リンクリスト内のサイクルを効率的に検出することができます。

2. **リンクリストの中央を見つける**：`fast`ポインターがリストの最後に到達するとき、`slow`ポインターはリストの真ん中に位置します。これを使用してリストの中央を見つけることができます。

3. **リンクリストのn番目の要素を見つける**：`fast`ポインターを`slow`ポインターよりnステップ先に配置します。このとき、`fast`がリストの末尾に達したとき、`slow`はリストのn番目の要素を指しています。

4. **リンクリストのパリティ（偶数または奇数の長さ）を判断する**：リストの最後に到達したとき、`fast`ポインターがnullを指している場合、リストは偶数の長さを持ち、`fast`が特定のノードを指している場合、リストは奇数の長さを持ちます。

これらの問題は、一度に1つの要素しか見ることができないリンクリストというデータ構造の制限を考えると、このアルゴリズムがなければ難しいかもしれません。したがって、このアルゴリズムは効率性と便利性のためにしばしば使われます。
"""