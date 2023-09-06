from collections import deque, Counter
from typing import List
import heapq

def leastInterval(tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque()  # pairs of [-cnt, idleTime]
    while maxHeap or q:
        time += 1

        if not maxHeap:
            time = q[0][1]
        else:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])
    return time
        
tasks = ["A","A","A","B","B","B"]
n = 2
print(leastInterval(tasks, n))
        
tasks = ["A","A","A","B","B","C","c"]
n = 2
print(leastInterval(tasks, n))

"""
このコードは、与えられたタスクのリストを、クールダウン期間`n`を考慮して最短時間で完了するための最少の時間を計算するためのものです。

**大まかな説明**:
タスクは頻度に基づいて最大ヒープに並べられ、最も頻繁に現れるタスクから順に処理されます。タスクが実行された後、そのタスクの次の実行が可能になるまでの待機時間が計算され、待機キューに追加されます。待機キュー内のタスクが再び実行可能になると、それは最大ヒープに戻されます。

**部分毎の説明**:
1. `count = Counter(tasks)`:
   `Counter`は各タスクの出現回数を計算します。

2. `maxHeap = [-cnt for cnt in count.values()]`:
   タスクの出現回数の逆数を使用してリストを作成します。逆数を使用する理由は、Pythonの標準ライブラリが最小ヒープしか提供していないため、最大ヒープをシミュレートする必要があるためです。

3. `heapq.heapify(maxHeap)`:
   上記で作成したリストをヒープに変換します。

4. `time = 0`と`q = deque()`:
   初期化段階です。`time`は経過時間を、`q`は待機キューを表します。

5. `while maxHeap or q`:
   最大ヒープまたは待機キューのいずれかに要素がある限り、ループを続けます。

6. `if not maxHeap: ...`:
   ヒープが空の場合、最も早く再実行可能になるタスクの再実行可能な時間に時間をジャンプさせます。

7. `else: ...`:
   ヒープからタスクを取り出し、そのタスクが再び実行可能になるまでの待機時間を計算し、待機キューに追加します。

8. `if q and q[0][1] == time: ...`:
   待機キューの先頭のタスクが再実行可能になった場合、そのタスクを最大ヒープに戻します。

9. `return time`:
   全てのタスクが終了したら、必要な最小の時間を返します。

このアプローチにより、タスクの頻度とクールダウンの制約を考慮して、必要な最小の時間を効率的に計算することができます。
"""