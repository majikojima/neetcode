from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
    res.append(newInterval)
    return res

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))

"""
このコードは、既存のソート済みの区間リスト`intervals`に新しい区間`newInterval`を挿入する問題の解法です。新しい区間は、既存の区間とオーバーラップするかもしれないので、このアルゴリズムはそのオーバーラップを処理します。

大まかな説明:
1. `res`という名前の結果リストを作成します。
2. 既存の各区間に対して、新しい区間をどこに挿入するかを判断します。
3. 既存の区間と新しい区間がオーバーラップしている場合、新しい区間を更新します。
4. 更新が完了したら、新しい区間を`res`に追加します。

部分毎の説明:
1. `res = []`: 結果として返す区間リストを初期化します。
2. `for i in range(len(intervals)):`: 既存の区間を順にチェックします。
3. `if newInterval[1] < intervals[i][0]:`: 新しい区間の終了が既存の区間の開始よりも前にある場合、新しい区間を`res`に追加し、残りの`intervals`を`res`に結合して結果を返します。
4. `elif newInterval[0] > intervals[i][1]:`: 新しい区間の開始が既存の区間の終了よりも後にある場合、既存の区間を`res`に追加します。
5. `else:`: 新しい区間と既存の区間がオーバーラップしている場合、新しい区間の開始と終了を適切に更新します。具体的には、開始は2つの区間の開始の最小値、終了は2つの区間の終了の最大値となります。
6. `res.append(newInterval)`: すべての既存の区間をチェックした後、更新された新しい区間（またはオーバーラップがない場合は元の新しい区間）を`res`に追加します。
7. `return res`: 更新された区間リストを返します。

このコードは、`intervals`がソート済みであることを前提としています。新しい区間が既存のいずれの区間ともオーバーラップしない場合、それは適切な位置に挿入されます。もしオーバーラップがある場合、新しい区間はそれに合わせて適切に更新され、結果リストに追加されます。
"""