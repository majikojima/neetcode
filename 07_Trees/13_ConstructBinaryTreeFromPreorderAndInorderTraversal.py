# Definition for a binary tree node.
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1 : mid + 1], inorder[:mid])
    root.right = buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
    return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
result = buildTree(preorder, inorder)
print(treeNode_to_list(result))

"""
このコードは、前順（preorder）と中順（inorder）のリストから二分木を再構築するためのものです。再帰的なアプローチを使用しています。

大まかな説明:
前順リストの最初の要素は二分木の根を示しています。この根を中順リストで見つけると、根の左側にあるすべての要素は左の部分木、根の右側にあるすべての要素は右の部分木になります。この情報を使用して、左と右の部分木を再帰的に構築します。

部分毎の説明:

1. 
   ```python
   if not preorder or not inorder:
       return None
   ```
   前順または中順のリストが空の場合、ノードは存在しないため、`None`を返します。

2. 
   ```python
   root = TreeNode(preorder[0])
   ```
   前順リストの最初の要素は常に根を示すため、新しいノードとしてこれを使用します。

3. 
   ```python
   mid = inorder.index(preorder[0])
   ```
   根の値を中順リストで見つけ、そのインデックスを取得します。このインデックスは、左部分木と右部分木を区別するために使用されます。

4. 
   ```python
   root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
   ```
   再帰的に左部分木を構築します。前順リストの最初の要素は根として使用されているため、その次の要素から左部分木の最後の要素までの範囲を考慮する必要があります。中順リストの場合は、根のインデックスの前のすべての要素が左部分木になります。

5. 
   ```python
   root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
   ```
   同様に、再帰的に右部分木を構築します。前順リストで左部分木の要素を超える部分から右部分木の要素が始まります。中順リストでは、根のインデックスの後のすべての要素が右部分木になります。

6. 
   ```python
   return root
   ```
   これで、左と右の部分木が構築され、完全な二分木が再構築されます。この再構築された木の根ノードを返します。
"""

"""
まず、前順（preorder）と中順（inorder）トラバースについて説明します。

1. **前順トラバース (Preorder Traversal)**:
   - まず現在のノードを訪問する。
   - 次に、左の子ノードに再帰的に前順トラバースを実行する。
   - 最後に、右の子ノードに再帰的に前順トラバースを実行する。

   たとえば、以下の二分探索木の場合:
   ```
       1
      / \
     2   3
    / \ / \
   4  5 6  7
   ```
   前順トラバースの結果は: `1, 2, 4, 5, 3, 6, 7`

2. **中順トラバース (Inorder Traversal)**:
   - まず、左の子ノードに再帰的に中順トラバースを実行する。
   - 次に現在のノードを訪問する。
   - 最後に、右の子ノードに再帰的に中順トラバースを実行する。

   例の二分探索木の場合:
   中順トラバースの結果は: `4, 2, 5, 1, 6, 3, 7`

問題文の内容に関して：
問題は、前順と中順トラバースの結果をもとに、元の二分木を再構築することを求めています。これは可能なのは、前順の最初の要素は根を示すためです。そして、この根を中順のリストで見つけると、それに基づいて左と右の子ノードのリストが明確になります。この情報を基にして再帰的に木を構築することができます。
"""

"""
`preorder`と`inorder`リストを使用して、二分木を再構築するプロセスをシミュレートします。

1. `preorder`の最初の要素は`3`です。これが私たちの根ノードになります。

2. `inorder`リストでこの根ノード（`3`）の位置を見つけると、それはインデックス`1`にあります。この位置を使用して、左部分木の要素と右部分木の要素を識別できます。
   - 左部分木の要素: `[9]`
   - 右部分木の要素: `[15,20,7]`

3. 左部分木を再帰的に構築します。
   - `preorder`リストの要素: `[9]`
   - `inorder`リストの要素: `[9]`

   ここで、`preorder`の最初の要素は`9`です。これは左部分木の根ノードです。このノードには左または右の子供はいないので、再帰はここで終了します。

4. 右部分木を再帰的に構築します。
   - `preorder`リストの要素: `[20,15,7]`
   - `inorder`リストの要素: `[15,20,7]`

   ここで、`preorder`の最初の要素は`20`です。これが右部分木の根ノードです。再び、この値を`inorder`リストで見つけます。この位置を使用して、左部分木の要素と右部分木の要素を再度識別できます。
   - 左部分木の要素: `[15]`
   - 右部分木の要素: `[7]`

5. `20`の左部分木を再帰的に構築します。
   - `preorder`リストの要素: `[15]`
   - `inorder`リストの要素: `[15]`
   
   これも葉ノードになるので、再帰は終了します。

6. `20`の右部分木を再帰的に構築します。
   - `preorder`リストの要素: `[7]`
   - `inorder`リストの要素: `[7]`
   
   これも葉ノードになるので、再帰は終了します。

再構築の結果として得られる二分木は以下のようになります：

```
    3
   / \
  9   20
     /  \
    15   7
```

このシミュレーションを通じて、`preorder`と`inorder`リストを使って二分木を効果的に再構築する方法がわかるはずです。
"""