# Definition for a binary tree node.
from typing import List
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

def rightSideView(root: TreeNode) -> List[int]:
    res = []
    q = deque([root])

    while q:
        rightSide = None
        qLen = len(q)

        for _ in range(qLen):
            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        if rightSide:
            res.append(rightSide.val)
    return res


root = [1,2,3,None,5,None,4]
print(root)
tree = list_to_treeNode(root)
print(rightSideView(tree))

"""
このコードは、与えられた二分木の「右側からの視点」のノードの値を順にリストとして返すものです。つまり、各深さのレベルで最も右側にあるノードの値をリストに追加しています。

コードの各部分の詳細な説明は以下の通りです：

1. `def rightSideView(self, root: TreeNode) -> List[int]:`
   - メソッドの定義部分。このメソッドは、二分木のrootノードを入力として受け取り、右側から見た時のノードの値をリストとして返す。

2. `res = []`
   - 結果を格納するためのリスト。

3. `q = collections.deque([root])`
   - 二分木のノードを探索するためのキュー。dequeを使用しています。

4. `while q:`
   - キューが空でない間、ループを続けます。

5. `rightSide = None`
   - 各レベルでの最も右側のノードを格納する変数。

6. `qLen = len(q)`
   - 現在のキューの長さ（つまり、現在のレベルのノード数）を取得します。

7. `for i in range(qLen):`
   - 現在のレベルの各ノードを順に探索するためのループ。

8. `node = q.popleft()`
   - キューの先頭からノードを取り出します。

9. `if node:`
   - ノードが存在する場合の処理。

10. `rightSide = node`
    - 取り出したノードをrightSideに格納します。

11. `q.append(node.left)` と `q.append(node.right)`
    - 現在のノードの左と右の子ノードをキューの末尾に追加します。

12. `if rightSide:`
    - rightSideが設定されている場合（つまり、現在のレベルでノードが存在する場合）の処理。

13. `res.append(rightSide.val)`
    - rightSideのノードの値を結果リストに追加します。

14. `return res`
    - 最終的な結果リストを返します。

このアルゴリズムは、幅優先探索 (BFS) を基にしており、各レベルの最後のノード（最も右側のノード）の値のみを結果リストに追加しています。
"""

"""
はい、そのとおりです！このアプローチのポイントは、`rightSide = node` の部分にあります。

各レベルのノードを順に探索する際、最後のノードがそのレベルでの最も右側のノードになります。したがって、ループの各ステップで `rightSide` を上書きすることで、ループの終わりには最も右側のノードだけが `rightSide` に残るというわけです。

このようなシンプルなアイデアを利用することで、コードは簡潔で効率的に動作します。幅優先探索を理解していると、このようなアイデアが自然と思い浮かぶこともあります。ただ、新しいアイデアやアプローチに出会うことは、プログラミングやアルゴリズムの学習において非常に有益です。一度このようなアイデアを学ぶと、似たような問題や状況でその知識を活用することができるようになります。
"""