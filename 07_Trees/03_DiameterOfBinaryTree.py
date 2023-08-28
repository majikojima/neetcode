# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)
        
        dfs(root)

        return res

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

root = [1,2,3,4,5]
print(root)
tree = list_to_treeNode(root)
result = s.diameterOfBinaryTree(tree)
print(result)

"""
コードは、二分木の直径を求めるためのものです。直径とは、木内の任意の2つのノード間の最長パス（エッジの数）のことを指します。これは、深さ優先探索（DFS）を使用して実装されています。

1. `def diameterOfBinaryTree(self, root: TreeNode) -> int:` - TreeNode型の引数を取り、その二分木の直径（整数）を返すメソッドを定義しています。

2. `res = 0` - 最長のパス（直径）を格納するための変数を初期化しています。

3. `def dfs(root):` - 深さ優先探索（DFS）を実装するための内部関数を定義しています。

4. `nonlocal res` - 内部関数から外部関数のローカル変数`res`にアクセスするための宣言です。

5. `if not root: return 0` - 現在のノードが存在しない場合（None）、深さは0であることを示します。

6. `left = dfs(root.left)` - 左の子ノードに対して深さ優先探索を行い、左側の最大深さを得ます。

7. `right = dfs(root.right)` - 右の子ノードに対して深さ優先探索を行い、右側の最大深さを得ます。

8. `res = max(res, left + right)` - 現在のノードをルートとする最長パス（左側の最大深さ + 右側の最大深さ）と、現在までの最長パス（res）の間で大きい方を新たな最長パスとして記録します。

9. `return 1 + max(left, right)` - 現在のノードを含む部分木の最大深さを返します（現在のノードを1とし、左部分木と右部分木の最大深さの大きい方と合計します）。

10. `dfs(root)` - ルートノードから深さ優先探索を開始します。

11. `return res` - 計算した最長パス（二分木の直径）を返します。
"""