# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def buildGraph(adjList):
    # ノードのリストを作成します。インデックスはval-1になるようにします。
    nodes = [Node(val=i+1) for i in range(len(adjList))]

    # adjListの各エントリについて隣接ノードを設定します。
    for i, neighbors in enumerate(adjList):
        for neighbor in neighbors:
            nodes[i].neighbors.append(nodes[neighbor-1])  # ノードのインデックスはval-1です。

    return nodes[0]  # 最初のノードを返します。

def cloneGraph(node: Node) -> Node:
    oldToNew = {}

    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        
        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node) if node else None
             
adjList = [[2,4],[1,3],[2,4],[1,3]]
graph = buildGraph(adjList)
print(cloneGraph(graph))

"""
この関数は、無向グラフのクローンを作成します。グラフの各ノードは、一意の値を持ち、隣接するノードのリストがあります。関数は、与えられたグラフのノード`node`から、そのクローンを返します。

**大まかな説明**:
この関数は、DFS（深さ優先探索）を利用して、与えられたノードから開始し、クローンノードを作成しながら全てのノードを訪問します。`oldToNew`辞書は、既存のノードからそのクローンまでのマッピングを追跡するのに使用されます。

**部分毎の説明**:

1. `oldToNew = {}`: これは、既存のノードからそのクローンまでのマッピングを保存する辞書です。

2. `def dfs(node):`: ヘルパー関数`dfs`を定義します。この関数は、与えられたノードのクローンを再帰的に作成します。

3. `if node in oldToNew:`: このノードがすでにクローンされたかどうかを確認します。

4. `copy = Node(node.val)`: 与えられたノードのクローンを作成します。

5. `oldToNew[node] = copy`: 現在のノードとそのクローンとの間のマッピングを保存します。

6. `for nei in node.neighbors:`: 現在のノードのすべての隣接ノードを繰り返し処理します。

7. `copy.neighbors.append(dfs(nei))`: 隣接ノードのクローンを作成し、それを現在のノードのクローンの隣接リストに追加します。

8. `return dfs(node) if node else None`: グラフが空でない場合、DFSを開始ノードで呼び出してクローンを返します。グラフが空の場合は、`None`を返します。
"""

"""
`adjList = [[2,4],[1,3],[2,4],[1,3]]`を使って、グラフを作成するプロセスをシミュレーションしていきます。

**ステップ1: `Node` インスタンスのリストを作成**

```python
nodes = [Node(val=i+1) for i in range(len(adjList))]
```

このコードは、`adjList`の長さ（4）だけ`Node`インスタンスを作成します。これにより、以下のようなノードのリストが作成されます：

1. Node(val=1, neighbors=[])
2. Node(val=2, neighbors=[])
3. Node(val=3, neighbors=[])
4. Node(val=4, neighbors=[])

**ステップ2: 各ノードに隣接するノードを割り当てる**

1つ目のエントリ`[2,4]`から始めます。これはノード1がノード2とノード4に隣接していることを示しています。

1. Node(val=1, neighbors=[Node2, Node4])
2. Node(val=2, neighbors=[])
3. Node(val=3, neighbors=[])
4. Node(val=4, neighbors=[])

次に、2つ目のエントリ`[1,3]`に移動します。これはノード2がノード1とノード3に隣接していることを示しています。

1. Node(val=1, neighbors=[Node2, Node4])
2. Node(val=2, neighbors=[Node1, Node3])
3. Node(val=3, neighbors=[])
4. Node(val=4, neighbors=[])

3つ目のエントリ`[2,4]`により、ノード3がノード2とノード4に隣接していることが示されています。そして、4つ目のエントリも同様です。

1. Node(val=1, neighbors=[Node2, Node4])
2. Node(val=2, neighbors=[Node1, Node3])
3. Node(val=3, neighbors=[Node2, Node4])
4. Node(val=4, neighbors=[Node1, Node3])

このようにして、`adjList`から`Node`クラスの形式でグラフが作成されました。
"""