from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    result = [1] * (len(nums))

    pre_result = [1] * (len(nums))
    prefix = 1
    for i in range(len(nums)):
        pre_result[i] = prefix
        prefix *= nums[i]

    print(f"pre_result: {pre_result}")

    post_result = [1] * (len(nums))
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        post_result[i] *= postfix
        postfix *= nums[i]

    print(f"post_result: {post_result}")

    for i in range(len(nums)):
        result[i] = pre_result[i] * post_result[i]

    return result

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