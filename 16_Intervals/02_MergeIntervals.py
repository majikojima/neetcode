from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda pair: pair[0])
    output = [intervals[0]]

    for start, end in intervals:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            # merge
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])
    return output

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))

intervals = [[1,4],[4,5]]
print(merge(intervals))

"""
このコードは、与えられた区間のリスト（`intervals`）を統合して重複しない区間のリストを返す関数`merge`を定義しています。大まかな流れとしては、まず区間のリストをスタートの時点でソートし、その後、ソートされた区間を走査して、結果のリストに順次区間を追加または統合していきます。

部分毎の説明を行います。

1. `intervals.sort(key=lambda pair: pair[0])`
   - `intervals`をその1つ目の要素（スタートの時点）に基づいてソートします。

2. `output = [intervals[0]]`
   - ソートされた`intervals`の最初の区間を`output`の初期値として設定します。

3. `for start, end in intervals:`
   - ソートされた`intervals`を一つずつ走査します。

4. `lastEnd = output[-1][1]`
   - 現在の`output`の最後の区間の終了時点を取得します。

5. `if start <= lastEnd:`
   - 現在の区間のスタートが、`output`の最後の区間の終了時点以下である場合、これらの区間は重複していると判断します。
   
6. `output[-1][1] = max(lastEnd, end)`
   - `output`の最後の区間の終了時点を、現在の区間の終了時点と比較して大きい方に更新します。これにより、重複する区間を統合します。

7. `else: output.append([start, end])`
   - 現在の区間が`output`の最後の区間と重複していない場合、`output`に現在の区間を追加します。

8. `return output`
   - 統合後の区間のリストを返します。

全体として、この関数は重複する区間を統合し、重複しない区間のリストを生成する役割を果たしています。
"""