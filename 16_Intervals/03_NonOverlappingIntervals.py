from typing import List

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort()
    res = 0
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)
    return res

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))

intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))

intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals))

"""
このコードは、与えられた区間のリストから、重複しないようにするために削除する必要がある区間の数を返す関数`eraseOverlapIntervals`を定義しています。

大まかな説明：
- 与えられた区間をスタート時点でソートします。
- 初めの区間を基準として、次の区間が重複しているかどうかをチェックします。
- 重複していれば、削除する区間の数を増やします。重複していなければ、参照する終了時点を更新します。

部分毎の説明：

1. `intervals.sort()`
   - 区間のリストをスタートの時点でソートします。

2. `res = 0`
   - 削除する必要がある区間の数を0で初期化します。

3. `prevEnd = intervals[0][1]`
   - ソートされた区間リストの最初の区間の終了時点を`prevEnd`として設定します。

4. `for start, end in intervals[1:]:`
   - ソートされた区間リストの2つ目から最後までを一つずつ走査します。

5. `if start >= prevEnd:`
   - 現在の区間のスタートが`prevEnd`以上であれば、前の区間と重複していないと判断します。

6. `prevEnd = end`
   - 重複していない場合、参照する終了時点を現在の区間の終了時点に更新します。

7. `else:`
   - 現在の区間が前の区間と重複している場合の処理。

8. `res += 1`
   - 重複する区間があれば、削除する区間の数を1増やします。

9. `prevEnd = min(end, prevEnd)`
   - 前の区間の終了時点と現在の区間の終了時点のうち、小さい方を新しい`prevEnd`として設定します。これは、次に考慮する区間が最も早く終了する区間とのみ重複しないようにするための戦略です。

10. `return res`
   - 削除する必要がある区間の数を返します。

この関数は、区間のリストから最小の区間の数を削除して、残りの区間が全て重複しないようにするための問題を解くのに役立ちます。
"""