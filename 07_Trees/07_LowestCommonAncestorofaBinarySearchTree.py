# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_treeNode(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    queue = deque([root])
    length = len(nums)
    index = 1

    while queue:
        node = queue.popleft()
        if index < length:
            if nums[index] is not None:
                node.left = TreeNode(nums[index])
                queue.append(node.left)
            index += 1
        if index < length:
            if nums[index] is not None:
                node.right = TreeNode(nums[index])
                queue.append(node.right)
            index += 1
    return root

def treeNode_to_list(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            if node.left or node.right or queue:  # Keep appending for remaining levels
                queue.append(node.left)
                queue.append(node.right)
        else:
            result.append(None)  # Keep appending None for missing nodes in this level
    while result[-1] is None:  # Remove trailing None values
        result.pop()
    return result

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    cur = root
    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur

root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 8

treer = list_to_treeNode(root)
treep = TreeNode(p)
treeq = TreeNode(q)
result = lowestCommonAncestor(treer, treep, treeq)
list = treeNode_to_list(result)
print(list)

p = 2
q = 4
treep = TreeNode(p)
treeq = TreeNode(q)
result = lowestCommonAncestor(treer, treep, treeq)
list = treeNode_to_list(result)
print(list)

"""
この関数は、二分探索木（Binary Search Tree、BST）における2つのノード`p`と`q`の最も低い共通の先祖（Lowest Common Ancestor、LCA）を返すものです。LCAは、2つのノード`p`と`q`の間に存在する最も深いノードであり、それぞれのノードが異なる子孫としてLCAの下に存在する場合を指します。

### 部分毎の説明:

1. **初期化**:
    ```python
    cur = root
    ```
    `cur`は現在調査しているノードを示します。最初は根ノードから探索を開始します。

2. **ノードの位置の確認**:
    ```python
    while cur:
    ```
    BSTのノードをトラバースしながらLCAを探します。

3. **`p`と`q`が現在のノードの右側にある場合**:
    ```python
    if p.val > cur.val and q.val > cur.val:
        cur = cur.right
    ```
    もし`p`と`q`の値が現在のノードの値よりも大きい場合、LCAは現在のノードの右側に存在するはずです。そのため、現在のノードを右の子ノードに更新します。

4. **`p`と`q`が現在のノードの左側にある場合**:
    ```python
    elif p.val < cur.val and q.val < cur.val:
        cur = cur.left
    ```
    もし`p`と`q`の値が現在のノードの値よりも小さい場合、LCAは現在のノードの左側に存在するはずです。そのため、現在のノードを左の子ノードに更新します。

5. **LCAの発見**:
    ```python
    else:
        return cur
    ```
    どちらの条件も満たされない場合（つまり、`p`と`q`が現在のノードの異なる側に存在する場合や、`p`や`q`のどちらかが現在のノードである場合）、現在のノードはLCAであると判断されます。

このアルゴリズムはBSTの性質を利用しているため、効率的にLCAを見つけることができます。
"""