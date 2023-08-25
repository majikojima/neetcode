from typing import List
import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    pts = []
    for x, y in points:
        dist = x**2 + y**2
        pts.append([dist, x, y])
    
    res = []
    heapq.heapify(pts)
    for _ in range(k):
        dist, x, y = heapq.heappop(pts)
        res.append([x, y])
    return res

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))

"""
この関数`kClosest`は、与えられた`points`の中から原点`(0,0)`に最も近い`k`個の点を返すものです。以下、その機能と部分毎の説明を行います。

## 大まかな説明:

1. 入力された各点について、原点からのユークリッド距離の2乗を計算します（平方根を取る必要はありません、なぜなら大小関係だけが重要なので）。
2. 計算された距離とその点の座標を一緒に保存します。
3. ヒープデータ構造を使用して、距離に基づいて点をソートします。
4. ヒープから最も近い`k`個の点を取り出して結果のリストに追加します。

## 部分毎の説明:

1. **変数の初期化**:
    ```python
    pts = []
    ```
    `pts`は、原点からの距離と、各点の座標を保存するためのリストです。

2. **距離の計算**:
    ```python
    for x, y in points:
        dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
        pts.append([dist, x, y])
    ```
    ここで、各点に対して原点からのユークリッド距離の2乗を計算し、それとともにその点の座標を`pts`に追加します。

3. **ヒープの作成**:
    ```python
    heapq.heapify(pts)
    ```
    `pts`をヒープデータ構造に変換します。ヒープは、最小値（または最大値）を効率的に取得できるデータ構造です。この場合、最小の距離を持つ点から順に取得したいので、最小ヒープを使用します。

4. **結果の作成**:
    ```python
    res = []
    for i in range(k):
        dist, x, y = heapq.heappop(pts)
        res.append([x, y])
    return res
    ```
    ヒープから最小の距離を持つ点を`k`回取り出し、その座標を結果のリスト`res`に追加します。最後に`res`を返します。

この関数は、与えられた点の中から原点に最も近い点を効率的に選択するためのもので、ヒープデータ構造を利用して高速化されています。
"""