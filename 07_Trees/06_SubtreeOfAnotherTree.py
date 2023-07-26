# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: TreeNode, q: TreeNode):
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

p = [3,4,5,1,2]
q = [4,1,2]
print(p,q)
pt = list_to_treeNode(p)
qt = list_to_treeNode(q)
result = s.isSubtree(pt,qt)
print(result)

p = [3,4,5,1,2,None,None,None,None,0]
q = [4,1,2]
print(p,q)
pt = list_to_treeNode(p)
qt = list_to_treeNode(q)
result = s.isSubtree(pt,qt)
print(result)

"""
この2つの関数は二分木内の部分木を探すために使用されます。

1. `def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:` - この関数は、指定された部分木(`subRoot`)が与えられたルートノード(`root`)から始まる二分木に存在するかどうかを判断します。

2. `if not subRoot:` - `subRoot`が`None`（すなわち、部分木が空）である場合、`True`を返します。空の部分木はどの木にも存在します。

3. `if not root:` - ルートが`None`（つまり、木が空）である場合、`False`を返します。部分木が存在するはずの木が空の場合、部分木は存在できません。

4. `if self.isSameTree(root, subRoot):` - `root`と`subRoot`が同じ木であるかどうかを確認します。同じであれば、`True`を返します。

5. `return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)` - ルートの左部分木または右部分木に部分木が存在するかどうかを確認します。どちらかに存在すれば`True`を返します。

6. `def isSameTree(self, p: TreeNode, q: TreeNode):` - `isSameTree`関数は前の質問で説明しました。この関数は、2つの木が全く同じであるかどうかを判断します。全てのノードの値が一致する場合にのみ`True`を返します。

7. `if not p and not q:` - `p`と`q`が共に`None`（つまり、どちらの木も空）であれば、`True`を返します。2つの空の木は同じと見なします。

8. `if p and q and p.val == q.val:` - `p`と`q`が共に存在し（つまり、どちらも`None`ではない）、かつそれぞれのノードの値が等しい場合、それぞれのノードの左部分木と右部分木も同じであるかを確認します。

9. `else:` - 2つのノードが等しくない場合、または一方が`None`で他方が`None`でない場合、`False`を返します。これは2つのツリーが同じではないことを示しています。
"""

"""
考えてみましょう：

    Tree 1:
      3
     / \
    4   5
   / \
  1   2

    SubTree:
     4
    / \
   1   2

となっているときに、以下のように動作します。

1. `isSubtree`を呼び出し、rootが3のTree1とrootが4のSubTreeを引数に取ります。

2. rootは`None`ではないので、まず`isSameTree`を呼び出して、rootが3のTree1とrootが4のSubTreeが同じ木であるかどうかを確認します。しかし、Tree1のroot値は3で、SubTreeのroot値は4なので、それらは同じではありません。したがって、`isSameTree`は`False`を返します。

3. `isSubtree`では、次にrootの左部分木（root値が4の部分木）とSubTreeが一致するかどうかを確認するために、再び`isSubtree`を呼び出します。

4. 今度は、root（値4）とSubTree（rootも4）が一致するかどうかを確認します。`isSameTree`を呼び出します。

5. 両方のrootの値は4なので、各rootの左部分木と右部分木が一致するかどうかを確認します。左部分木は1で、右部分木は2で、これらはSubTreeと一致します。したがって、`isSameTree`は`True`を返します。

6. `isSubtree`は、root（値が4のノード）とSubTreeが一致するため、`True`を返します。これにより、SubTreeはTree1に含まれていると確認されます。
"""