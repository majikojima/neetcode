from typing import List

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    par = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)

    def find(n):
        p = par[n]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p

    # return False if already unioned
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False
        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]

edges = [[1,2],[1,3],[2,3]]
print(findRedundantConnection(edges))

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(findRedundantConnection(edges))

"""
このコードは、与えられたエッジのリスト（`edges`）から、グラフを閉じる（サイクルを作る）冗長な接続（エッジ）を探し出すためのものです。これは、Union-Find（またはDisjoint Set Union、DSU）というアルゴリズムを利用しています。

**全体の説明:**  
各ノードの親（`par`）とそのランク（`rank`）を保持する配列を初期化します。エッジを1つずつ処理し、2つのノードを結合（`union`）します。もし結合しようとするノードが既に同じセットに属していれば、そのエッジは冗長なので返します。

**部分毎の説明:**  

1. `par = [i for i in range(len(edges) + 1)]`
   - 各ノードの親を示す配列を初期化します。初めは各ノードが自分自身を親とします。

2. `rank = [1] * (len(edges) + 1)`
   - 各ノードのランクを示す配列を初期化します。初めは1で始まります。

3. `def find(n):`
   - 与えられたノードの最上位の親（ルート）を見つけるための関数。

4. `while p != par[p]:`
   - ノードの親が自分自身でない限り、親をたどります。

5. `def union(n1, n2):`
   - 2つのノードを結合する関数。もし2つのノードが同じセットに属していれば、`False`を返し、それ以外の場合は`True`を返します。

6. `if p1 == p2:`
   - 2つのノードが同じセットに属していれば、`False`を返します。

7. `for n1, n2 in edges:`
   - 与えられたエッジを順番に処理します。

8. `if not union(n1, n2):`
   - エッジの2つのノードを結合しようとします。もし結合できなかった場合（すなわち、2つのノードが既に同じセットに属している場合）、そのエッジは冗長なので返します。

このアルゴリズムの目的は、グラフ内のサイクルを検出することです。サイクルが存在する場合、その最後のエッジが冗長な接続となります。
"""