from typing import List
import collections
import heapq

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    edges = collections.defaultdict(list)
    for u, v, w in times:
        edges[u].append((v, w))

    minHeap = [(0, k)]
    visit = set()
    t = 0
    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in visit:
            continue
        visit.add(n1)
        t = w1

        for n2, w2 in edges[n1]:
            if n2 not in visit:
                heapq.heappush(minHeap, (w1 + w2, n2))
    return t if len(visit) == n else -1

    # O(E * logV)

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))

times = [[1,2,1]]
n = 2
k = 1
print(networkDelayTime(times, n, k))

times = [[1,2,1]]
n = 2
k = 2
print(networkDelayTime(times, n, k))

"""
このコードは、指定された始点からのネットワーク上のすべてのノードへの最短遅延時間を計算します。具体的には、各`times`要素が形式`[u, v, w]`で提供される有向グラフが与えられた場合、ノード`u`からノード`v`までの遅延時間`w`を示します。関数は、指定された始点`k`からすべてのノードへの信号が伝播するのにかかる最大時間を返します。すべてのノードに信号が到達しない場合、関数は-1を返します。

コードの大まかな流れと部分ごとの説明は以下の通りです：

1. **エッジの情報を保存**：
    ```python
    edges = collections.defaultdict(list)
    for u, v, w in times:
        edges[u].append((v, w))
    ```
    `edges`というdefaultdictに、各ノードから出るエッジの情報（隣接ノードとそのエッジの重み）を保存します。

2. **初期化**：
    ```python
    minHeap = [(0, k)]
    visit = set()
    t = 0
    ```
    `minHeap`はDijkstraのアルゴリズムで使用されるプライオリティキュー、`visit`は訪問済みのノードを記録するセット、`t`は現在の最大遅延時間を表します。

3. **Dijkstraのアルゴリズムの実行**：
    ```python
    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in visit:
            continue
        visit.add(n1)
        t = w1

        for n2, w2 in edges[n1]:
            if n2 not in visit:
                heapq.heappush(minHeap, (w1 + w2, n2))
    ```
    この部分はDijkstraのアルゴリズムを使用して、指定された始点からのすべてのノードへの最短遅延時間を計算します。

4. **結果の確認と返却**：
    ```python
    return t if len(visit) == n else -1
    ```
    すべてのノードが訪問された場合、`t`を返します。訪問されなかったノードがある場合、-1を返します。

5. **時間複雑度のコメント**：
    ```python
    # O(E * logV)
    ```
    このコメントは、コードの時間複雑度がエッジの数`E`とlog(ノードの数`V`)の積であることを示しています。これはDijkstraのアルゴリズムをヒープを使用して実装した場合の時間複雑度です。
"""

"""
このコードは、Dijkstraのアルゴリズムを使用して、指定された始点からのネットワーク上のすべてのノードへの最短遅延時間を計算する部分です。

1. **ヒープからの要素の取り出し**：
    ```python
    w1, n1 = heapq.heappop(minHeap)
    ```
    `minHeap`という優先度付きキューから最小の重みを持つエッジを取り出します。ここで、`w1`は取り出されたエッジの重み、`n1`はそのエッジの終点ノードを示します。

2. **訪問済みノードの確認**：
    ```python
    if n1 in visit:
        continue
    ```
    `n1`がすでに訪問済みの場合、そのエッジは無視され、ループの次のイテレーションに進みます。

3. **ノードの訪問と最大遅延時間の更新**：
    ```python
    visit.add(n1)
    t = w1
    ```
    `n1`を訪問済みノードのセットに追加し、現在の最大遅延時間を`w1`に更新します。

4. **隣接ノードの探索とヒープへの追加**：
    ```python
    for n2, w2 in edges[n1]:
        if n2 not in visit:
            heapq.heappush(minHeap, (w1 + w2, n2))
    ```
    このループでは、`n1`からのすべての隣接ノードとそのエッジの重みを調べます。未訪問の隣接ノード`n2`について、始点からの総遅延時間（これまでの遅延時間`w1`と現在のエッジの遅延時間`w2`の和）とそのノードをヒープに追加します。これにより、未訪問のノードについては、始点からの最短遅延時間の順にヒープから取り出され、処理されることになります。

このコードの実行を通じて、Dijkstraのアルゴリズムは始点からのすべてのノードへの最短遅延時間を効率的に計算することができます。
"""

"""
times = [[2,1,1],[2,3,1],[3,4,1]]、n = 4、k = 2 で `networkDelayTime` メソッドの動作をシミュレートします。

まず、初期の準備を確認しましょう。

1. `edges` ディクショナリを作成します。キーは出発ノード、値は（到着ノード, 重み）のタプルのリストです。
2. 最初のノード（k）の遅延時間を0に設定し、そのノードをminHeapに追加します。
3. `visit` セットを空のセットとして初期化します。これは、訪問済みのノードを追跡します。
4. `t` は最後に訪問したノードの遅延時間を格納します。これは最終的に返される値になります。

**シミュレーション開始**:

minHeap = [(0, 2)]（k = 2からの遅延時間は0）

**1回目のループ**:
- w1, n1 = (0, 2)
- n1 (つまり2) はまだ訪問されていないので、それを訪問セットに追加します。
- t = 0
- n1 (つまり2) からのエッジを調べます：(1,1) と (3,1)
- これらのエッジはminHeapに追加されます。

minHeap = [(1,1), (1,3)]

**2回目のループ**:
- w1, n1 = (1,1)
- n1 (つまり1) はまだ訪問されていないので、それを訪問セットに追加します。
- t = 1
- n1 (つまり1) からのエッジはありません。

minHeap = [(1,3)]

**3回目のループ**:
- w1, n1 = (1,3)
- n1 (つまり3) はまだ訪問されていないので、それを訪問セットに追加します。
- t = 1
- n1 (つまり3) からのエッジを調べます：(4,1)
- このエッジはminHeapに追加されます。

minHeap = [(2,4)]

**4回目のループ**:
- w1, n1 = (2,4)
- n1 (つまり4) はまだ訪問されていないので、それを訪問セットに追加します。
- t = 2
- n1 (つまり4) からのエッジはありません。

最後に、すべてのノードが訪問されているかどうかを確認します。それらは訪問されていますので、`t` の値である2が返されます。
"""