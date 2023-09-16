from collections import defaultdict
from typing import List

class DetectSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res

D = DetectSquares()
print(D.add((3,10)))
print(D.add((11,2)))
print(D.add((3,2)))
print(D.count((11,10)))
print(D.count((14,8)))
print(D.add((11,2)))
print(D.count((11,10)))

"""
このクラス `DetectSquares` は、2次元平面上の点の集合を追跡して、与えられた点を1つの角として持つ正方形の数をカウントすることができます。

**大まかな説明**:
- `DetectSquares` のインスタンスは、追加された点のカウントと点のリストを持っています。
- `add` メソッドは、点を追加します。
- `count` メソッドは、指定された点を1つの角として持つ正方形の数を返します。

**部分毎の説明**:

1. **初期化**:
    ```python
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []
    ```
    - `ptsCount` は各点の出現回数を追跡するための辞書です。
    - `pts` は追加された点のリストです。

2. **点の追加**:
    ```python
    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)
    ```
    - 与えられた点の出現回数を増やします。
    - その点をリストに追加します。

3. **正方形のカウント**:
    ```python
    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res
    ```
    - `px, py` は与えられた点の座標です。
    - 各点 `x, y` に対して、その点が正方形の対角の角である場合（`abs(py - y) == abs(px - x)`）かつ、`x` が `px` と異なり、`y` が `py` と異なる場合にのみ正方形を形成します。
    - カウントは、`x` で `py` のy座標を持つ点と、`px` で `y` のy座標を持つ点の出現回数の積として計算されます。これは、正方形を形成するために必要な他の2つの角の出現回数に基づいています。

このアルゴリズムは、指定された点に対して正方形の数を効果的にカウントするためのシンプルな方法を提供します。
"""