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
    
             
adjList = [[2,4],[1,3],[2,4],[1,3]]
graph = buildGraph(adjList)
print(cloneGraph(graph))