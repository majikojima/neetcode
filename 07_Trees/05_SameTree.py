# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


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

s = Solution()

p = [1,2,3]
q = [1,2,3]
print(p,q)
pt = list_to_treeNode(p)
qt = list_to_treeNode(q)
result = s.isSameTree(pt,qt)
print(result)

p = [1,2]
q = [1,None,2]
print(p,q)
pt = list_to_treeNode(p)
qt = list_to_treeNode(q)
result = s.isSameTree(pt,qt)
print(result)

"""
この関数は二つの二分木`p`と`q`が同じかどうかを判断します。

1. `if not p and not q:` - この行では、`p`と`q`が共に`None`（つまり、いずれの木もノードを持っていない）かどうかを確認します。この場合、2つの空の木は同じであると判断し、`True`を返します。

2. `if p and q and p.val == q.val:` - この行では、`p`と`q`が共に存在し（つまり、どちらも`None`ではない）、かつそれぞれのノードの値が等しいかどうかを確認します。この場合、それぞれのノードの左の子ノードと右の子ノードも同じであるか確認します。

3. `return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)` - `p`の左の子ノードと`q`の左の子ノードが同じで、`p`の右の子ノードと`q`の右の子ノードが同じである場合にのみ`True`を返します。この行は再帰的に呼び出され、全ての子ノードが一致するまでチェックします。

4. `else:` - `p`と`q`が`None`ではなく、その値が等しくない場合、または一方が`None`で他方が`None`でない場合には、`False`を返します。これは2つのツリーが同じではないことを示しています。
"""