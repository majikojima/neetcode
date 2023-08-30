from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    pre = [1] * len(nums)
    n = 1
    for i in range(len(nums)):
        pre[i] = n
        n = n * nums[i]
    print(pre)

    suf = [1] * len(nums)
    n = 1
    for i in range(len(nums)-1, -1, -1):
        suf[i] = n
        n = n * nums[i]
    print(suf)

    res = [1] * len(nums)
    for i in range(len(nums)):
        res[i] = pre[i] * suf[i]
    
    return res

nums = [1,2,3,4]
result = productExceptSelf(nums)

print(result)

"""
あなたのコードは、以前のコードの詳細なバージョンと見なすことができます。前方の積と後方の積を分かりやすく示すために、それぞれの計算結果を別々のリストに保存しています。

このコードの概要は次のとおりです：

1. `result`, `pre_result`, `post_result` という3つのリストを初期化します。すべての要素は `1` で、`nums` の長さと同じです。

2. `pre_result` を計算します。このリストは、各要素の前方にあるすべての要素の積を保存します。

3. `post_result` を計算します。このリストは、各要素の後方にあるすべての要素の積を保存します。

4. 最後に、`pre_result` と `post_result` の要素を乗算して、答えの `result` リストを得ます。

実行すると、以下のような結果が得られます：

```
pre_result: [1, 1, 2, 6]
post_result: [24, 12, 4, 1]
[24, 12, 8, 6]
```

このコードは、前方の積と後方の積の計算方法を明確に示しており、初学者にとって理解しやすいと思います。不思議なアルゴリズムの背後にある考え方を理解する手助けとなるでしょう。
"""