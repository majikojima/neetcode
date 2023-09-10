from typing import List
import heapq

def minCostConnectPoints(points: List[List[int]]) -> int:
    N = len(points)
    adj = {i: [] for i in range(N)}  # i : list of [cost, node]
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    # Prim's
    res = 0
    visit = set()
    minH = [[0, 0]]  # [cost, point]
    while len(visit) < N:
        cost, i = heapq.heappop(minH)
        if i in visit:
            continue
        res += cost
        visit.add(i)
        for neiCost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minH, [neiCost, nei])
    return res

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(minCostConnectPoints(points))

points = [[3,12],[-2,5],[-4,1]]
print(minCostConnectPoints(points))

"""
このコードは、与えられた点のリストの間の最小のコストで全ての点を接続するためのコストを計算するためのものです。具体的には、このコードはPrimのアルゴリズムを使用して最小全域木を見つけます。全域木とは、グラフ内の全ての頂点を含む木のことで、最小全域木はその中で辺の重みの合計が最小のものを指します。

**全体の説明:**  
点のすべてのペア間の距離を計算し、それらの距離を基に隣接リストを作成します。次に、Primのアルゴリズムを使用して最小全域木のコストを計算します。

**部分毎の説明:** 

1. `N = len(points)`: 
   - 点の総数を取得します。

2. `adj = {i: [] for i in range(N)}`:
   - 各点の隣接リストを初期化します。

3. `for i in range(N):`
   - 各点に対して、他のすべての点との間のマンハッタン距離を計算し、隣接リストにその情報を追加します。

4. `dist = abs(x1 - x2) + abs(y1 - y2)`:
   - マンハッタン距離を計算します。

5. `# Prim's`:
   - ここからPrimのアルゴリズムの実装が始まります。

6. `minH = [[0, 0]]`: 
   - 最小ヒープを初期化し、最初の点（index 0）のコストを0として追加します。

7. `while len(visit) < N:`:
   - すべての点が訪問されるまでループを続けます。

8. `if i in visit:`:
   - 現在の点が既に訪問されている場合、次の点を処理します。

9. `res += cost`:
   - 現在の点へのコストを結果に追加します。

10. `for neiCost, nei in adj[i]:`:
    - 現在の点のすべての隣接点を処理し、それらの点がまだ訪問されていない場合、その点とコストを最小ヒープに追加します。

このアルゴリズムは、与えられた点を最小のコストで接続する方法を見つけるための効率的な方法を提供します。Primのアルゴリズムは、最小全域木を見つけるためのグリーディアルゴリズムの一つです。
"""

"""
この部分は、Primのアルゴリズムを使用して、点の集合から最小全域木を見つけるためのものです。このアルゴリズムは、各ステップで現在のノードから選ばれた最小のエッジを持つノードを追加することで動作します。

詳細に説明すると：

1. **初期化**:
   - `res = 0`: 最小全域木の全コストを保存するための変数を初期化します。
   - `visit = set()`: これまでに訪問した点を追跡するためのセットを初期化します。
   - `minH = [[0, 0]]`: 最小ヒープを初期化し、最初の点（index 0）のコストを0としてセットします。

2. **アルゴリズムの実行**:
   - `while len(visit) < N:`: すべての点が訪問されるまでループを続けます。
   
3. **現在の最小のコストを持つエッジの取得**:
   - `cost, i = heapq.heappop(minH)`: ヒープから最小のコストを持つエッジを取り出します。
   
4. **訪問済みの点のスキップ**:
   - `if i in visit:`: 現在の点が既に訪問されている場合、このループの残りの部分をスキップして次の点を処理します。
   
5. **最小のエッジのコストの追加**:
   - `res += cost`: 現在の点への最小のエッジのコストを結果に追加します。

6. **現在の点の訪問のマーキング**:
   - `visit.add(i)`: 現在の点を訪問済みとしてマークします。

7. **隣接点の処理**:
   - `for neiCost, nei in adj[i]:`: 現在の点のすべての隣接点をループします。
   - `if nei not in visit:`: 隣接点がまだ訪問されていない場合のみ、以下の処理を行います。
   - `heapq.heappush(minH, [neiCost, nei])`: 隣接点とそのエッジのコストをヒープにプッシュします。これにより、次のステップで最小のエッジを持つ点が選択されます。

8. **結果の返却**:
   - `return res`: 最小全域木のコストを返します。

このPrimのアルゴリズムの実装は、最小ヒープを使用して効率的に動作します。ヒープは、各ステップで最小のエッジのコストを持つ点を迅速に見つけるためのものです。
"""