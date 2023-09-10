from typing import List

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # dfs
    prereq = {i: [] for i in range(numCourses)}

    # map each course to : prereq list
    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    output = []
    visit, cycle = set(), set()

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True

        cycle.add(crs)
        for pre in prereq[crs]:
            if not dfs(pre):
                return False
        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True

    for c in range(numCourses):
        if not dfs(c):
            return []
    return output

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses, prerequisites))

numCourses = 6
prerequisites = [[0,1],[0,2],[1,3],[3,2],[4,0],[5,0]]
print(findOrder(numCourses, prerequisites))

"""
このコードは、与えられたコースの数（`numCourses`）とその前提条件（`prerequisites`）を考慮して、コースを完了するための順序を返すものです。これは、トポロジカルソートの一種の問題として考えられます。特定のコースを完了するためには、その前提条件のコースを先に完了させる必要があります。

**全体の説明:**  
前提条件（`prerequisites`）をもとにグラフを作成します。次に、DFSを使用してサイクルを検出し、トポロジカルソートを行います。

**部分毎の説明:**  

1. `prereq = {c: [] for c in range(numCourses)}`
   - 各コースの前提条件を保存するための辞書を初期化します。

2. `for crs, pre in prerequisites:`
   - 与えられた前提条件を処理して、`prereq`辞書を更新します。

3. `output = []`
   - 最終的なコースの順序を保存するためのリスト。

4. `visit, cycle = set(), set()`
   - `visit`: すでに訪問済みのノード（コース）を保存するためのセット。
   - `cycle`: 現在のDFSの探索パスにあるノードを保存するセット（サイクルの検出に使用）。

5. `def dfs(crs):`
   - コースを順番に訪問し、サイクルがないことを確認しながらトポロジカルソートを行うDFS関数。

6. `if crs in cycle:`
   - 現在のコースがサイクルセットにある場合、サイクルが検出されるので、`False`を返します。

7. `if crs in visit:`
   - すでに訪問済みのノードは再度訪問する必要がないので、`True`を返します。

8. `cycle.add(crs)`
   - 現在のコースをサイクルセットに追加します。

9. `for pre in prereq[crs]:`
   - 現在のコースの前提条件を順番に訪問します。

10. `cycle.remove(crs)`
   - コースの探索が終了したので、サイクルセットから削除します。

11. `visit.add(crs)`
    - コースを訪問済みとしてマークします。

12. `output.append(crs)`
    - トポロジカルソートの順序に従ってコースを`output`リストに追加します。

13. `for c in range(numCourses):`
    - すべてのコースについてDFSを実行します。

14. `if dfs(c) == False:`
    - サイクルが検出された場合、空のリストを返します。

15. `return output`
    - トポロジカルソートの結果としてのコースの順序を返します。
"""