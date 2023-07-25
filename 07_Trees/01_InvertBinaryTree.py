# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

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

s = Solution()

root = [4,2,7,1,3,6,9]
print(root)
tree = list_to_treeNode(root)
result = s.invertTree(tree)
list = treeNode_to_list(result)
print(list)


"""
もちろんです。以下に各行の説明を行います：

1. `from collections import deque`: Pythonのcollectionsモジュールからdequeをインポートします。dequeは、両端から効率的にアイテムを追加または削除できる特殊な種類のリストです。ここでは、ツリーノードを幅優先探索（BFS）で管理するために使用します。

2. `def list_to_treeNode(nums):` この行は、`list_to_treeNode`という新しい関数を定義します。この関数は、整数のリスト（nums）を入力として受け取り、そのリストを使ってバイナリツリーを作成します。

3. `if not nums:` この行は、与えられたリストが空であるかどうかをチェックします。空の場合、関数はNoneを返します。

4. `root = TreeNode(nums[0])`: リストの最初の要素から新しいTreeNodeを作成し、それをバイナリツリーの根として設定します。

5. `queue = deque([root])`: deque（二重終端キュー）を初期化し、最初の要素としてルートノードを追加します。

6. `length = len(nums)`: この行は、入力リストの長さを計算し、その結果を変数`length`に保存します。

7. `index = 1`: `index`という新しい変数を作成し、値を1に設定します。この`index`は、作業している現在のリストの要素のインデックスを示します。

8. `while queue:`: この行は、キューが空になるまで（つまり、すべてのノードが処理されるまで）ループを開始します。

9. `node = queue.popleft()`: dequeの最初のノードを取り出し、それを現在作業しているノードとして設定します。

10-14. `if index < length:` の内部：このコードブロックでは、現在のノードの左の子供を設定します。リスト内の対応する位置の値がNoneでない場合、その値から新しいTreeNodeを作成し、それを現在のノードの左の子供として設定します。また、新しく作成したノードをdequeの末尾に追加します。最後に、`index`を1つ増やして次のリストの要素に移動します。

15-19. 再度、`if index < length:` の内部：このコードブロックでは、現在のノードの右の子供を設定します。基本的なプロセスは左の子供を設定するときと同じです。

20. `return root`: 最後に、この関数は作成したバイナリツリーの根ノードを返します。

この関数は、リストを入力として取り、対応するバイナリツリーを出力として返すという目的を達成しています。リストは、ツリーのノードをレベル順に（上から下へ、左から右へ）格納しています。
"""

"""
この関数は、与えられた二分木を"反転"または"鏡像化"します。1行ずつ見ていきましょう。

1. `def invertTree(self, root: TreeNode) -> TreeNode:`  
   これは、このメソッドが名前付きであることを示しています。これは`invertTree`と呼ばれ、引数として`root`(ルートノード)を取り、戻り値として`TreeNode`型を返します。

2. `if not root:`  
   これは、rootが`None`(つまり、空のツリーが与えられた場合)であるかどうかを確認します。もしrootが`None`であれば、次の行が実行されます。

3. `return None`  
   これは、rootが`None`の場合、すなわち、与えられたツリーが空の場合、`None`を返します。

4. `tmp = root.left`  
   一時的な変数`tmp`に、rootの左子ノードを保存します。

5. `root.left = root.right`  
   rootの左子ノードに、rootの右子ノードを指定します。これにより、左右の子ノードが入れ替わる一部となります。

6. `root.right = tmp`  
   rootの右子ノードに、先程一時的に保存した元の左子ノード(つまり`tmp`)を指定します。これにより、左右の子ノードの入れ替えが完了します。

7. `self.invertTree(root.left)`  
   再帰的に左子ノードに対して同じ操作を行います。つまり、左子ノードをrootと見なしたときに、その下の部分ツリーを反転します。

8. `self.invertTree(root.right)`  
   同様に、再帰的に右子ノードに対して同じ操作を行います。つまり、右子ノードをrootと見なしたときに、その下の部分ツリーを反転します。

9. `return root`  
   最後に、反転が完了したツリーのルートノードを返します。これが新しく反転したツリーのルートノードになります。

以上のように、この関数は二分木の左右の子ノードを再帰的に反転することで、二分木全体を反転します。
"""

"""
もちろんです。以下に各行の説明を記述します：

1. `from collections import deque`: `collections` モジュールから `deque` というデータ型をインポートします。`deque`は双方向キューで、両端に対する追加や削除が効率的に行えます。

2. `def treeNode_to_list(root):` : `treeNode_to_list` という関数を定義しています。この関数は、二分木の根（root）を引数として受け取り、その二分木をリスト形式に変換します。

3. `if not root:` : この行では、二分木の根が存在しない（None）かどうかをチェックしています。

4. `return []`: 二分木の根が存在しない場合、空のリストを返します。

5. `queue = deque([root])`: 根のノードから始めるキューを作成します。

6. `result = []`: 二分木のノードの値を格納するための結果リストを初期化します。

7. `while queue:`: キューが空になるまで、つまりすべてのノードが処理されるまでループを続けます。

8. `node = queue.popleft()`: キューから先頭のノードを取り出します。

9. `if node:`: 取り出したノードがNoneではない（つまり実際のTreeNodeオブジェクトである）ことを確認します。

10. `result.append(node.val)`: ノードの値を結果リストに追加します。

11. `if node.left or node.right or queue:`: 左の子ノード、右の子ノード、またはキューにまだノードがある場合（つまり、まだ処理すべきレベルが残っている場合）に進みます。

12. `queue.append(node.left)`, `queue.append(node.right)`: 左と右の子ノードをキューの末尾に追加します。

13. `else:`: 取り出したノードがNone（実際のノードではなく、欠けているノードを示す）である場合に進みます。

14. `result.append(None)`: この欠けているノードをリストにNoneとして追加します。

15. `while result[-1] is None:`: 結果リストの最後の要素がNoneである間（つまり、最後のレベルにノードがない間）ループを続けます。

16. `result.pop()`: 最後のNoneを結果リストから削除します。

17. `return result`: 変換したリストを返します。

この関数は、入力として与えられた二分木をリストに変換します。このリストは、レベルオーダートラバーサル（つまり、上から下へ、左から右へ）でノードの値を格納します。なお、欠けているノードはNoneとして格納されます。
"""