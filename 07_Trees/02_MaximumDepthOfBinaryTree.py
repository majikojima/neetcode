from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        print(f"val:{root.val}")
        print(f"left:{root.left}, right:{root.right}")
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

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
result = s.maxDepth(tree)
print(result)

"""
こちらのコードは、与えられた二分木（root）の最大深度を計算するためのものです。それぞれの行が何をやっているかを説明します：

1. **def maxDepth(self, root: TreeNode) -> int:** ここでは、関数`maxDepth`を定義しています。引数として`root`（二分木の根）を取り、返り値の型は整数（二分木の最大深度）であることを示しています。

2. **if not root:** ここでは、`root`がNone（つまり、二分木が空である）かどうかを確認しています。もし`root`がNoneなら、その二分木の深度は0なので、次の行で0を返します。

3. **return 0:** 二分木が空である（`root`がNone）場合、その深度は0なので、0を返します。

4. **return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)):** ここでは、再帰的に二分木の最大深度を計算しています。二分木の最大深度は、「根から最も深い葉までのパスの長さ」です。根から左部分木の最大深度と右部分木の最大深度のうち、より大きな値に1（根自身）を加えたものが全体の最大深度となります。

このコードは、"深さ優先探索"（Depth-First Search, DFS）というアルゴリズムを用いて、二分木の最大深度を求めています。
"""

"""
この行が二分木の深さを求める理由をもう少し詳しく説明します。

二分木の深さとは、根から最も遠い葉までのエッジの数です。つまり、根から最も深いノードまでのパスの長さを求めています。その最も基本的な方法は、左の部分木と右の部分木の深さのうち大きい方に1（現在のノード）を加えることです。

たとえば以下の二分木を考えてみましょう。

```
    1
   / \
  2   3
 / \   
4   5 
```

この二分木の深さを求めるために、まず左部分木と右部分木のどちらの深さが大きいかを比較します。

- 左部分木は以下のようになります。

```
  2
 / \
4   5
```
ここで最大深さは2です（2->4 または 2->5 のパス）。

- 右部分木は以下のようになります。

```
  3
```
ここで最大深さは1です（3のみ）。

したがって、元の二分木の深さは、左部分木と右部分木の深さの大きい方（ここでは2）に1を加えたもの、つまり3になります。

このプロセスは再帰的に行われます。つまり、各ノードでそのノードを根とする部分木の深さを求め、それを上位のノードの深さの計算に使用します。このアルゴリズムでは、「現在のノード」を根とする部分木の深さを求めるために、そのノードの左の子ノードと右の子ノードを根とする部分木の深さを再帰的に計算しています。

この方法では、各ノードを1回ずつ訪れるだけで二分木の深さを効率的に計算できます。
"""