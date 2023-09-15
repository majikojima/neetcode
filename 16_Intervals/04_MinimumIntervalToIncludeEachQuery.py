from typing import List
import heapq

def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    intervals.sort()
    minHeap = []
    res = {}
    i = 0
    for q in sorted(queries):
        while i < len(intervals) and intervals[i][0] <= q:
            l, r = intervals[i]
            heapq.heappush(minHeap, (r - l + 1, r))
            i += 1

        while minHeap and minHeap[0][1] < q:
            heapq.heappop(minHeap)
        res[q] = minHeap[0][0] if minHeap else -1
    return [res[q] for q in queries]

intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]
print(minInterval(intervals, queries))

intervals = [[2,3],[2,5],[1,8],[20,25]]
queries = [2,19,5,22]
print(minInterval(intervals, queries))

"""
このコードは、指定されたクエリポイントごとに最小の区間を見つけ、その区間の長さを返す関数`minInterval`を定義しています。

大まかな説明:
- 与えられた区間をスタートの時点でソートします。
- クエリもソートして処理します。
- クエリの各ポイントについて、それを含む可能性のあるすべての区間をミニマムヒープに追加します。
- 現在のクエリポイントよりも早く終わる区間はヒープから削除します。
- 最小の区間はヒープのトップにあります。
- 各クエリの結果を辞書で保存し、最後に指定されたクエリの順序で結果を返します。

部分毎の説明:

1. `intervals.sort()`
   - 区間をスタート時点でソートします。

2. `minHeap = []`
   - ミニマムヒープを初期化します。

3. `res = {}`
   - 各クエリの結果を保存するための辞書を初期化します。

4. `i = 0`
   - 現在の区間のインデックスを初期化します。

5. `for q in sorted(queries):`
   - ソートされたクエリに対して反復処理を行います。

6. `while i < len(intervals) and intervals[i][0] <= q:`
   - 現在のクエリポイントをカバーする可能性のあるすべての区間をヒープに追加します。

7. `heapq.heappush(minHeap, (r - l + 1, r))`
   - 区間の長さと終了時点をヒープに追加します。区間の長さは優先的にヒープの順序付けのために使われます。

8. `while minHeap and minHeap[0][1] < q:`
   - 現在のクエリポイントよりも前に終了する区間は、もはや考慮する必要がないのでヒープから削除します。

9. `res[q] = minHeap[0][0] if minHeap else -1`
   - クエリポイントに一致する最小の区間の長さを辞書に保存します。ヒープが空の場合は-1を保存します。

10. `return [res[q] for q in queries]`
   - 最後に、指定されたクエリの順序で結果をリストとして返します。

この関数は、各クエリポイントに対して最小の区間の長さを高速に見つけるのに役立ちます。
"""