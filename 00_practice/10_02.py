from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def b(i, curr, total):
        if total == target:
            # res.append(curr)
            res.append(curr.copy())
            return
        if total > target:
            return
        if i >= len(candidates):
            return
        curr.append(candidates[i])
        b(i, curr, total + candidates[i])

        curr.pop()
        b(i + 1, curr, total)
        
    b(0, [], 0)
    return res

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))

"""
提供された`combinationSum`関数には、期待される結果が得られない主な理由があります。それは、リスト`curr`を関数の中で変更していることに起因します。

具体的には、次のコード行において：

```python
res.append(curr)
```

ここで`curr`リストの参照を`res`に追加していますが、`curr`リストそのものが後続の操作で変更されています（例: `curr.pop()`）。このため、`res`に保存されたリストも後から変更されてしまい、最終的な結果が期待したものと異なることが発生します。

この問題を解決するために、新しいリストとして`curr`のコピーを`res`に追加する必要があります。これは、以下のように`curr.copy()`を使用して行います：

```python
res.append(curr.copy())
```

これにより、関数は期待する結果を返すようになります。
"""