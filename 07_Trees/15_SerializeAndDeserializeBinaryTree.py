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

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

root = [1,2,3,None,None,4,5]
print(root)
tree = list_to_treeNode(root)

codec = Codec()
s = codec.serialize(tree)
print(s)

ans = codec.deserialize(s)

list = treeNode_to_list(ans)
print(list)

"""
このコードは、二分木のシリアライズとデシリアライズを行うためのクラス、`Codec`を定義しています。

### 大まかな説明：
`Codec` クラスは、二分木を文字列に変換（シリアライズ）したり、文字列を二分木に変換（デシリアライズ）したりするための2つのメソッドを持っています。

- `serialize` メソッドは、二分木をコンマ区切りの文字列に変換します。
- `deserialize` メソッドは、コンマ区切りの文字列を二分木に変換します。

### 部分毎の説明：

#### serialize

1. `res` というリストを初期化します。これは、ノードの値を保存するためのものです。
2. `dfs` というヘルパーメソッドを定義します。これは、二分木を深さ優先探索でトラバースするためのものです。
   - ノードが存在しない場合、リスト `res` に `"N"`（Noneを示す）を追加します。
   - ノードが存在する場合、そのノードの値を `res` に追加し、左の子ノードと右の子ノードに対しても同じ操作を再帰的に行います。
3. ルートノードから `dfs` を呼び出して探索を開始します。
4. 最後に、`res` の各要素をコンマで結合して、一つの文字列として返します。

#### deserialize

1. 引数として与えられた文字列 `data` をコンマで分割し、`vals` リストに格納します。
2. `self.i` というインデックスを 0 で初期化します。これは、`vals` の現在の要素を追跡するためのものです。
3. `dfs` というヘルパーメソッドを定義します。これは、リスト `vals` の値を使用して、二分木を再構築するためのものです。
   - 現在のインデックス `self.i` の値が `"N"` の場合、Noneを返します。
   - それ以外の場合、現在の値を使用して新しいノードを作成し、左の子ノードと右の子ノードに対しても同じ操作を再帰的に行います。
4. 最後に、`dfs` を呼び出して、リスト `vals` の値を使用して二分木を再構築し、ルートノードを返します。
"""