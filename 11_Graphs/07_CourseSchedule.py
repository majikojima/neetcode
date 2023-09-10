from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # dfs
    preMap = {i: [] for i in range(numCourses)}

    # map each course to : prereq list
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visiting = set()

    def dfs(crs):
        if crs in visiting:
            return False
        if preMap[crs] == []:
            return True

        visiting.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visiting.remove(crs)
        preMap[crs] = []
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False
    return True

numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))

numCourses = 5
prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]]
print(canFinish(numCourses, prerequisites))

numCourses = 3
prerequisites = [[0,1],[1,2],[2,0]]
print(canFinish(numCourses, prerequisites))

"""
このコードは、指定されたコースとその前提条件を満たしてすべてのコースを完了できるかどうかを判断するものです。具体的には、これはトポロジカルソーティングの問題と関連しており、各コースとその前提条件をグラフとして表現し、そのグラフにサイクルが存在しないかどうかを確認します。サイクルが存在する場合、コースは完了できません。

コードの部分毎の説明：

1. `preMap = {i: [] for i in range(numCourses)}`
    - 各コースに対する前提条件リストを格納するためのマップを初期化します。

2. `for crs, pre in prerequisites:`
    - このループは前提条件のリストを走査し、`preMap`に各コースの前提条件を追加します。

3. `visiting = set()`
    - 現在訪問中のノード（またはコース）を追跡するためのセットを初期化します。このセットはDFSがサイクルを検出するのに役立ちます。

4. `def dfs(crs):`
    - 深さ優先探索 (DFS) を行うためのヘルパー関数です。この関数は指定されたコースが前提条件なしで完了できるか、またはその前提条件がサイクルなしで完了できるかどうかを確認します。

5. `for c in range(numCourses):`
    - すべてのコースに対してDFSを実行します。どれかのコースでDFSが`False`を返す場合、すべてのコースを完了することはできません。

このアルゴリズムは、深さ優先探索を利用してグラフ内のサイクルを効果的に検出します。サイクルが存在する場合、すべてのコースを完了することはできません。
"""

"""
この`dfs`関数は深さ優先探索 (DFS) のアルゴリズムを用いて、指定されたコース（`crs`）が他の前提条件なしで完了できるか、または前提条件がサイクルなしで完了できるかどうかを確認するヘルパー関数です。

以下、関数内の各行の詳しい説明を行います。

1. `if crs in visiting:`
   - すでに訪問中のコース（ノード）を再度訪問しようとすると、これはグラフにサイクルが存在することを示すため、`False`を返します。

2. `if preMap[crs] == []:`
   - `crs`コースに前提条件がなければ、それは自由に取ることができるので、`True`を返します。

3. `visiting.add(crs)`
   - 現在訪問中のコースとして`crs`をマークします。これにより、以降のDFSの呼び出しで同じコースを再度訪問する場合を検出できます。

4. `for pre in preMap[crs]:`
   - `crs`コースの前提条件（`pre`）を一つずつ調査します。

5. `if not dfs(pre):`
   - 前提条件`pre`のコースに対して再帰的にDFSを呼び出します。これにより、`pre`コースがサイクルなしで完了できるかどうかを確認します。もし`pre`コースがサイクルを持っていたり、その他の理由で完了できない場合は、`False`を返して現在のコース`crs`も完了できないことを示します。

6. `visiting.remove(crs)`
   - `crs`コースの訪問が終了したので、`visiting`セットから削除します。

7. `preMap[crs] = []`
   - `crs`コースとその前提条件に関する探索が終了したため、前提条件リストをクリアして以降の探索を効率的にします。

8. `return True`
   - このコースとそのすべての前提条件をサイクルなしで完了できるため、`True`を返します。

この`dfs`関数は、前提条件のチェーンがサイクルを形成していないかどうかをチェックするのに役立ちます。サイクルが存在する場合、コースのシーケンスを完了することはできません。
"""