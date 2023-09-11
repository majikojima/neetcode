import heapq

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())

"""
このコードは、数の動的なリストから中央値を効率的に取得するためのデータ構造を実装しています。実装のキーは、2つのヒープ（最大ヒープと最小ヒープ）を使用して、数をバランスよく保持することです。

**大まかな説明**:
- `MedianFinder`は、数を追加して中央値を効率的に取得するためのクラスです。
- 2つのヒープ（`small`と`large`）を使用して、数の半分を保持します。`small`は最大ヒープとして動作し、`large`は最小ヒープとして動作します。
- `addNum`メソッドは、数を適切なヒープに追加し、ヒープのバランスを維持します。
- `findMedian`メソッドは、2つのヒープのトップ要素を使用して中央値を計算します。

**部分毎の説明**:

1. **`__init__`メソッド**:
   - 2つのヒープ（`small`と`large`）を初期化します。`small`は、負の数として数を保存することで、最大ヒープとして動作します。`large`は、デフォルトの最小ヒープとして動作します。

2. **`addNum`メソッド**:
   - まず、`num`が`large`ヒープのトップ要素よりも大きい場合、`large`に`num`をプッシュします。それ以外の場合は、`small`に`num`を負の値としてプッシュします。
   - 次に、2つのヒープのサイズの差が1を超える場合、大きい方のヒープのトップ要素を小さい方のヒープに移動して、バランスを取り戻します。

3. **`findMedian`メソッド**:
   - `small`が`large`よりも要素が多い場合、`small`のトップ要素（最大値）が中央値となります。
   - 逆に、`large`が`small`よりも要素が多い場合、`large`のトップ要素（最小値）が中央値となります。
   - 2つのヒープが同じサイズの場合、2つのヒープのトップ要素の平均値が中央値となります。

この実装により、数の追加がO(log N)の時間内で行われ、中央値の取得がO(1)の時間内で行われることが保証されます。
"""