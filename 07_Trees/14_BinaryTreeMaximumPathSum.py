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

def maxPathSum(root: TreeNode) -> int:
    res = [root.val]

    def dfs(root):
        if not root:
            return 0
        
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        res[0] = max(res[0], root.val + leftMax + rightMax)
        return root.val + max(leftMax, rightMax)
    
    dfs(root)
    return res[0]

root = [-10,9,20,None,None,15,7]
print(root)
tree = list_to_treeNode(root)
print(maxPathSum(tree))

"""
このコードは、与えられたバイナリツリーにおける任意のノード間の最大パスの合計を返すものです。ここでの「パス」とは、ツリー上の任意のノードから開始して、下向きに移動して終わるノードまでの連続したノードのシーケンスを意味します。

コードの詳細な説明：

1. **res = [root.val]**
    - `res`は、最大パスの合計を格納するためのリストです。ミュータブルなリストとして初期化されるのは、内部関数`dfs`から非ミュータブルなスコープにアクセスするためです。初期値は`root.val`に設定されています。

2. **dfs(root):**
    - `dfs`は、与えられたノードからの最大パスの合計を返す深さ優先探索のヘルパー関数です。この関数は「分岐」（左と右の子への両方のパス）を考慮しません。

3. **leftMax = dfs(root.left)** と **rightMax = dfs(root.right)**
    - 現在のノードの左と右の子からの最大パスの合計を取得します。

4. **leftMax = max(leftMax, 0)** と **rightMax = max(rightMax, 0)**
    - パスの合計が負の場合、それを考慮しないように0と比較して最大値を取ります。

5. **res[0] = max(res[0], root.val + leftMax + rightMax)**
    - ここでは「分岐」を考慮して、左の子と右の子を含む現在のノードの最大パスの合計を計算します。そして、それがこれまでの最大値よりも大きい場合には、最大値を更新します。

6. **return root.val + max(leftMax, rightMax)**
    - 最後に、現在のノードからの最大パスの合計を返します（ただし、左または右の子のどちらか一方のみを考慮します）。

7. 最後に、`dfs(root)`を呼び出して全体の最大パスの合計を計算し、`res[0]`を返します。

このアルゴリズムの鍵は、各ノードで左と右の子を含む最大のパスの合計を計算しながら、同時に左または右の子のどちらか一方だけを含むパスの合計も計算する点にあります。
"""

"""
質問に答える前に、Pythonの関数内での変数の扱いに関する基本的な事実を考慮してください。Pythonでは、整数、浮動小数点数、文字列などの基本データ型はイミュータブル（変更不可能）です。したがって、関数の内部から外部の変数を変更することはできません。しかし、リストや辞書のようなミュータブルなオブジェクトは関数の内部から変更することができます。

1. **なぜ、resはlistなの？**
    `res`はリストとして定義されていますので、`dfs`関数の内部からグローバルな`res`変数を変更できます。もし`res`が整数として定義されていた場合、`dfs`関数の中でその値を変更することはできませんでした。`res`をリストとして使用することで、`dfs`関数の中から`res[0]`を更新することができます。

2. **なぜ、return root.val + max(leftMax, rightMax)で、leftとrightのどっちかのmaxをとるの？**
    この関数の目的は、与えられたノードを起点として、左または右の子ノードの方向に進むことで得られる最大のパスの合計を計算することです。つまり、左と右の子ノードの両方を同時に通るようなパスは考慮していません。そのため、左の子ノードと右の子ノードの最大のパスの合計のうち、大きい方の値を選ぶ必要があります。それが`max(leftMax, rightMax)`の部分です。

    しかし、これだけでは全ての可能なパスをカバーしていないため、`res[0] = max(res[0], root.val + leftMax + rightMax)`の行が存在します。この行では、左の子ノードと右の子ノードの両方を通るパスの合計を計算しています。これにより、すべての可能なパスが考慮され、最大のものが`res[0]`に格納されます。
"""

"""
与えられたコードと、ツリー構造 `root = [-10,9,20,None,None,15,7]` を使用してシミュレーションします。

ツリーは以下のように見えます。

```
    -10
   /   \
  9     20
       /  \
      15   7
```

`maxPathSum` 関数のシミュレーションを行います:

1. 初期設定：`res = [-10]`

2. `-10` から開始します。
    * `leftMax = dfs(9)` から開始します。
        - `9` の左の子ノードは `None` です。したがって、`leftMax = 0` となります。
        - `9` の右の子ノードも `None` です。したがって、`rightMax = 0` となります。
        - `res[0] = max(-10, 9 + 0 + 0) = max(-10, 9) = 9`
        - このノードからの最大のパスは `9` なので、`return 9` となります。
    * `leftMax = 9`
    * 次に、`rightMax = dfs(20)` を実行します。
        - `20` の左の子ノードは `15` です。
            + `15` の左、右の子ノードは両方とも `None` ですので、`leftMax` と `rightMax` は `0` となります。
            + `res[0] = max(9, 15 + 0 + 0) = max(9, 15) = 15`
            + `return 15` となります。
        - `20` の右の子ノードは `7` です。
            + `7` の左、右の子ノードは両方とも `None` ですので、`leftMax` と `rightMax` は `0` となります。
            + `res[0] = max(15, 7 + 0 + 0) = max(15, 7) = 15`
            + `return 7` となります。
        - `20` の左からの最大パスは `15` で、右からの最大パスは `7` です。
        - `res[0] = max(15, 20 + 15 + 7) = max(15, 42) = 42`
        - `return 20 + max(15, 7) = 35` となります。
    * `rightMax = 35`
    * この段階で、`res[0] = max(42, -10 + 9 + 35) = max(42, 34) = 42`
    * 最後の行は `return -10 + max(9, 35) = 25` となりますが、この値は最終的な結果として返されるわけではありません。

3. `return res[0]` により、最終的な答えとして `42` が返されます。

したがって、このツリーの最大のパスの合計は `42` となります。
"""