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

def kthSmallest(root: TreeNode, k: int) -> int:
    def inorder(node):
        if node:
            return inorder(node.left) + [node.val] + inorder(node.right)
        else:
            return []
        
    return inorder(root)[k - 1]

root = [3,1,4,None,2]
k = 1
print(root)
tree = list_to_treeNode(root)
print(kthSmallest(tree, k))

root = [4,2,5,None,3]
k = 3
print(root)
tree = list_to_treeNode(root)
print(kthSmallest(tree, k))

"""
正しく`kthSmallest`を実装するための一つのアプローチとして、二分探索木の中順巡回を利用します。中順巡回は二分探索木の要素を小さい順に列挙する特性を持っています。中順巡回を使って`kthSmallest`を正しく実装しています

このアプローチは、全てのノードの値をリストに格納し、その後にk番目の要素を返します。より効率的なアプローチも考えられますが、この方法は理解しやすく、実装も直感的です。
"""

"""
指定された二分探索木と`kthSmallest`関数を使ってk番目に小さい要素を見つける手順をシミュレートします。

まず、木の構造:
```
    4
   / \
  2   5
   \
    3
```

関数のシミュレーション：

1. `inorder`関数は中順（In-Order）で木をトラバースし、すべての要素をリストとして返します。

2. 最初に、`kthSmallest`関数が呼び出されると、中順トラバースによって生成されたリストのk-1番目の要素が返されることになります。

シミュレーションを進めてみましょう：

1. 最初にroot（4）からスタートします。
2. まず左の子（2）の中順トラバースが実行されます。
   - 2の左の子は存在しないので、`[]`が返されます。
   - その後、2自体の値を返します：`[2]`
   - 2の右の子（3）の中順トラバースが実行されます。
     - 3の左右の子は存在しないので、`[]`が返され、3自体の値が返されます：`[3]`
   - したがって、2を根とする部分木の中順トラバースの結果は`[2, 3]`です。
   
3. 次にroot（4）自体の値を返します：`[4]`

4. 4の右の子（5）の中順トラバースが実行されます。
   - 5の左右の子は存在しないので、`[]`が返され、5自体の値が返されます：`[5]`
   
5. これにより、全体の中順トラバースの結果は`[2, 3, 4, 5]`となります。

最後に、このリストのk-1=2番目の要素は3なので、k=3の要素は3となります。
"""