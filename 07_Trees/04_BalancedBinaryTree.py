# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1+max(left[1], right[1])]
        
        return dfs(root)[0]

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

root = [3,9,20,None,None,15,7]
print(root)
tree = list_to_treeNode(root)
result = s.isBalanced(tree)
print(result)

root = [1,2,2,3,3,None,None,4,4]
print(root)
tree = list_to_treeNode(root)
result = s.isBalanced(tree)
print(result)

"""
このコードは、与えられた二分木がバランスされているかどうかをチェックします。バランスされた二分木とは、すべてのノードについてその左部分木と右部分木の高さが最大でも1しか違わないものを指します。

1. `def isBalanced(self, root: TreeNode) -> bool:` - TreeNode型の引数を取り、その二分木がバランスされているかどうかをブール値で返すメソッドを定義しています。

2. `def dfs(root):` - バランスチェックと高さの計算を行うための深さ優先探索（DFS）を実装するための内部関数を定義しています。

3. `if not root: return [True, 0]` - 現在のノードが存在しない場合（None）、そのノードは自動的にバランスしている（True）とし、高さは0であるとします。

4. `left = dfs(root.left)` - 左の子ノードに対して深さ優先探索を行い、そのノードがバランスしているかとその高さを得ます。

5. `right = dfs(root.right)` - 右の子ノードに対して深さ優先探索を行い、そのノードがバランスしているかとその高さを得ます。

6. `balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1` - 現在のノードがバランスしているかどうかをチェックします。これは、左の子ノードと右の子ノードが両方ともバランスしていて、かつ、左部分木と右部分木の高さの差が1以下であるときにのみTrueになります。

7. `return [balanced, 1+max(left[1], right[1])]` - 現在のノードがバランスしているか（ブール値）とその高さ（現在のノードを1とし、左部分木と右部分木の高さの大きい方と合計します）のリストを返します。

8. `return dfs(root)[0]` - ルートノードから深さ優先探索を開始し、その結果からバランスチェックの結果（ブール値）を返します。
"""