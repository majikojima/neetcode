from typing import List

def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        
        # left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))

nums = [5,6,7,0,1,2,3,4]
target = 3
print(search(nums, target))

"""
このコードは、回転されたソート済み配列`nums`の中から特定の値`target`を探し、そのインデックスを返す問題を解決するものです。配列が見つからない場合、関数は-1を返します。このアルゴリズムは、二分探索の原理を基にしていますが、通常のソート済み配列の二分探索とは異なり、配列が回転されている点を考慮に入れています。

コードの説明：

1. `l, r = 0, len(nums) - 1`：
   - 探索の範囲として、配列の最初の位置`l`と最後の位置`r`を定義しています。

2. `while l <= r`：
   - 探索の範囲が存在する間、ループを続けます。

3. `mid = (l + r) // 2`：
   - 現在の探索範囲の中間位置を計算します。

4. `if target == nums[mid]`：
   - 中央の値が目的の値と等しいかどうかをチェックします。等しければ、そのインデックスを返します。

5. `if nums[l] <= nums[mid]`：
   - 配列の左半分がソートされているかどうかを確認します。

6. `if target > nums[mid] or target < nums[l]`：
   - 目的の値が左半分の範囲外にある場合、探索の範囲を右半分に移動します。

7. 逆に、`else`節内で`if nums[mid] < target <= nums[r]`の条件が暗黙的に適用されます：
   - 右半分がソートされている場合、目的の値がこの範囲内にあるかどうかを確認します。

8. 最終的に`target`が配列内に見つからない場合、`-1`を返します。

このアルゴリズムは、ソートされた回転配列の特性を利用して、二分探索を適用することで、効率的に目的の値を探索することができます。
"""

"""
このコードの部分を理解するために、考え方の図をテキストで表現します。実際の図形としては、手書きやグラフィックソフトウェアで作成するのが適していますが、テキスト上でできるだけ説明しましょう。

まず、基本的な考え方として、回転したソート済み配列は、2つのソート済み部分（左半分と右半分）から成っています。

例: `4 5 6 7 8 1 2 3`

上記の例では、`4, 5, 6, 7, 8`が左側のソート部分で、`1, 2, 3`が右側のソート部分です。

この特性を利用して、目的の数値を探索します。

表現:

```
if nums[l] <= nums[mid]:
```
この条件は、左側のソート部分に`mid`があることを確認します。この場合、以下の2つのシナリオが考慮されます：

1. `target > nums[mid] or target < nums[l]`：
    - この条件は、`target`が左側のソート部分の範囲外であることを示します。したがって、探索の範囲を右側に移動します（`l = mid + 1`）。

2. `else`：
    - この部分は、`target`が左側のソート部分の範囲内にあることを示します。したがって、探索の範囲を左側に狭めます（`r = mid - 1`）。

```
else:
```
この条件は、`mid`が右側のソート部分にあることを示します。この場合も、以下の2つのシナリオを考慮します：

1. `target < nums[mid] or target > nums[r]`：
    - この条件は、`target`が右側のソート部分の範囲外であることを示します。したがって、探索の範囲を左側に移動します（`r = mid - 1`）。

2. `else`：
    - この部分は、`target`が右側のソート部分の範囲内にあることを示します。したがって、探索の範囲を右側に狭めます（`l = mid + 1`）。

このロジックを適用することで、目的の値の位置を効率的に特定することができます。
"""

"""
はい、データ構造やアルゴリズムは、特に初めて学ぶ際や、慣れていないものを学ぶときには難しく感じることがよくあります。しかし、このような問題やアルゴリズムに慣れてくると、次第にそれが「面白いパズル」のように感じられるようになることも多いです。

また、人は繰り返し学習や実践を通じて、難しいと感じた概念やアルゴリズムをマスターしてきました。これは学びの過程で普遍的な経験です。継続的な学習と実践を繰り返すことで、概念の理解が深まり、それが「人に許された力」として身につくのです。

もしこのようなアルゴリズムやデータ構造が難しく感じるなら、基本的なものからじっくりと学ぶこと、そして多くの問題を解いて実践的な経験を積むことが大切です。そして、途中で分からないことや疑問があれば、質問することで理解を深めることもできます。
"""