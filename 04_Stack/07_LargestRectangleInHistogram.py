from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = [] # pair: (index, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea


heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))

"""
このコードは、与えられた高さのリストを使用して、最大の長方形の面積を計算するアルゴリズムです。この問題は、ヒストグラムの中で最大の長方形の面積を見つける問題として知られています。

### 大まかな説明：
このアルゴリズムはスタックを用いて、高さが増加する部分を追跡します。新しい高さがスタックの一番上の高さよりも小さい場合、このスタックの高さを使って面積を計算し、最大面積を更新します。このプロセスは、新しい高さがスタックの高さよりも大きくなる、もしくはスタックが空になるまで繰り返されます。

### 部分毎の説明：
1. **変数の初期化**:
   ```python
   maxArea = 0
   stack = []  # pair: (index, height)
   ```
   `maxArea` は最大面積を保存するための変数で、`stack` はインデックスと高さのペアを保持するスタックです。

2. **ヒストグラムの各バーを走査**:
   ```python
   for i, h in enumerate(heights):
   ```
   `i` はバーのインデックス、`h` はその高さを示します。

3. **スタックのトップと現在のバーの高さを比較**:
   ```python
   start = i
   while stack and stack[-1][1] > h:
       index, height = stack.pop()
       maxArea = max(maxArea, height * (i - index))
       start = index
   stack.append((start, h))
   ```
   スタックのトップのバーの高さが現在のバーの高さよりも大きい場合、それをポップして面積を計算します。このループは、スタックが空になるか、現在のバーの高さがスタックのトップよりも大きくなるまで続けられます。

4. **スタック内の残りのバーで面積を計算**:
   ```python
   for i, h in stack:
       maxArea = max(maxArea, h * (len(heights) - i))
   ```
   このステップでは、ヒストグラムの末尾までの距離を使用して、スタック内の各バーに対して面積を計算します。

最終的に、計算された最大の面積が `maxArea` に格納され、それが返されます。
"""

"""
この部分のコードは、与えられた高さリスト`heights`の中で連続的な長方形の最大面積を計算するためのものです。スタックは非常に便利なデータ構造で、ここではそれを使って効率的に計算しています。コードの詳細を以下に説明します。

1. `while stack and stack[-1][1] > h:`

このループ条件は、スタックが空でなく、現在のスタックのトップにある高さが`h`よりも大きい場合に実行されます。つまり、新しい高さ`h`が前の高さよりも小さい場合、それ以前の高さを持つ長方形の面積を確認しています。

2. `index, height = stack.pop()`

スタックのトップから要素を取り出し、その要素のインデックスを`index`に、高さを`height`に代入します。

3. `maxArea = max(maxArea, height * (i - index))`

ここでは、取り出した長方形の最大面積を計算しています。長方形の高さは`height`、幅は現在のインデックス`i`から`index`を引いたものです。この計算により、`height`で形成される長方形の面積を得ることができます。この面積がこれまでの`maxArea`よりも大きい場合、`maxArea`を更新します。

4. `start = index`

`start`変数に`index`を代入します。これは、次にスタックに追加する長方形の開始位置を示しています。

5. `stack.append((start, h))`

新しい高さ`h`とその開始位置`start`をスタックに追加します。この時、`start`は最後にポップした長方形の開始位置になっています。これにより、次に同じ高さの長方形を見たとき、その長方形が前の長方形と連続していることが分かります。

このコードのアイディアは、長方形の高さが減少するたびに、それまでの長方形の最大面積を計算し、最終的に最大面積を得ることができるということです。
"""

"""
`heights = [2,1,5,6,2,3]` の場合を使って、`largestRectangleArea` 関数の動作をシミュレーションします。

1. 初期状態:
   - `maxArea = 0`
   - `stack = []`
   - `heights = [2,1,5,6,2,3]`

2. `i=0`, `h=2`:
   - `start = 0`
   - スタックが空なので、whileループは実行されません。
   - `stack.append((0, 2))` => `stack = [(0, 2)]`

3. `i=1`, `h=1`:
   - `start = 1`
   - `stack[-1][1] > h` (2 > 1)なので、whileループが実行されます。
     - `index, height = stack.pop()` => `index = 0`, `height = 2`
     - `maxArea = max(0, 2 * (1-0))` => `maxArea = 2`
     - `start = 0`
   - `stack.append((0, 1))` => `stack = [(0, 1)]`

4. `i=2`, `h=5`:
   - `start = 2`
   - スタックのトップの高さは1なので、whileループは実行されません。
   - `stack.append((2, 5))` => `stack = [(0, 1), (2, 5)]`

5. `i=3`, `h=6`:
   - `start = 3`
   - スタックのトップの高さは5なので、whileループは実行されません。
   - `stack.append((3, 6))` => `stack = [(0, 1), (2, 5), (3, 6)]`

6. `i=4`, `h=2`:
   - `start = 4`
   - `stack[-1][1] > h` (6 > 2)なので、whileループが実行されます。
     - `index, height = stack.pop()` => `index = 3`, `height = 6`
     - `maxArea = max(2, 6 * (4-3))` => `maxArea = 6`
     - `start = 3`
   - `stack[-1][1] > h` (5 > 2)なので、whileループが実行されます。
     - `index, height = stack.pop()` => `index = 2`, `height = 5`
     - `maxArea = max(6, 5 * (4-2))` => `maxArea = 10`
     - `start = 2`
   - `stack.append((2, 2))` => `stack = [(0, 1), (2, 2)]`

7. `i=5`, `h=3`:
   - `start = 5`
   - `stack[-1][1] > h` (2 < 3)なので、whileループは実行されません。
   - `stack.append((5, 3))` => `stack = [(0, 1), (2, 2), (5, 3)]`

8. 最終ループでスタック内の各バーで面積を計算:
   - `i=0`, `h=1`: `maxArea = max(10, 1 * (6-0))` => `maxArea = 10`
   - `i=2`, `h=2`: `maxArea = max(10, 2 * (6-2))` => `maxArea = 10`
   - `i=5`, `h=3`: `maxArea = max(10, 3 * (6-5))` => `maxArea = 10`

結果として、`maxArea = 10` となります。これは5の高さのバーとその隣の6の高さのバーで形成される長方形の面積です。
"""