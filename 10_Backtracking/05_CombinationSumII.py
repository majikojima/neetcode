from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def backtrack(cur, pos, target):
        if target == 0:
            res.append(cur[:])
            return
        if target <= 0:
            return
        
        prev = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue
            cur.append(candidates[i])
            backtrack(cur, i + 1, target - candidates[i])
            cur.pop()
            prev = candidates[i]

    backtrack([], 0, target)
    return res


candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates, target))

"""
この関数`combinationSum2`は、与えられた候補数字のリストから、与えられたターゲットになるような組み合わせを探します。重複する数字があっても、各組み合わせは一意でなければなりません。

大まかな説明:
- `combinationSum2`関数は、`candidates`リストから、`target`に等しい合計値を持つ組み合わせのリストを返す関数です。
- 重複する組み合わせを避けるために、`candidates`をソートします。
- バックトラッキングアルゴリズムを使用して、可能なすべての組み合わせを探索します。

部分毎の説明:
1. `candidates.sort()`: 候補のリストをソートします。このソートにより、重複する組み合わせを回避するのが簡単になります。
2. `res = []`: 解の組み合わせを格納するリストを初期化します。
3. `backtrack`関数の定義:
   - `cur`: 現在の組み合わせを表すリスト。
   - `pos`: 候補のリスト内での現在の位置。
   - `target`: 現在のターゲットから`cur`内の数字を引いた値。
   - `if target == 0:`: 現在の組み合わせの合計がターゲットに等しい場合、結果にこの組み合わせを追加します。
   - `if target <= 0:`: ターゲットが0未満または等しい場合、これ以上の組み合わせを探索する必要はありません。
   - `prev = -1`: これは前回調べた数字を格納します。重複する組み合わせを回避するために使用されます。
   - `for i in range(pos, len(candidates)):`: `pos`から始めて、候補のリストのすべての要素に対してループします。
     - `if candidates[i] == prev:`: 前回のループと同じ数字をスキップします。
     - `cur.append(candidates[i])`: 現在の数字を組み合わせに追加します。
     - `backtrack(cur, i + 1, target - candidates[i])`: 再帰的に次の数字を調べるためのバックトラック。
     - `cur.pop()`: 現在の数字を組み合わせから取り除きます。
     - `prev = candidates[i]`: 前回の数字を更新します。
4. `backtrack([], 0, target)`: バックトラッキングの初期呼び出し。空の組み合わせ、位置0、与えられたターゲットからスタートします。
5. `return res`: 最終的な組み合わせのリストを返します。
"""

"""
了解しました。`candidates = [10,1,2,7,6,1,5]`と`target = 8`を使って、`combinationSum2`関数の動作をシミュレーションします。

1. 最初に、candidatesをソートします。  
   `candidates = [1,1,2,5,6,7,10]`

2. `backtrack`関数を`([], 0, 8)`で呼び出します。
   - `cur = []`, `pos = 0`, `target = 8`, `prev = -1`（初期値）

3. 0番目の要素、`candidates[0]`（つまり1）をチェックします。
   - `cur = [1]`, `target = 7`になります。
   - 新しい`backtrack`を`([1], 1, 7)`で呼び出します。

4. この新しい`backtrack`内で、1番目の要素、`candidates[1]`（つまり1）をチェックします。
   - `cur = [1, 1]`, `target = 6`になります。
   - 新しい`backtrack`を`([1, 1], 2, 6)`で呼び出します。

5. この新しい`backtrack`内で、2番目の要素、`candidates[2]`（つまり2）をチェックします。
   - `cur = [1, 1, 2]`, `target = 4`になります。
   - 新しい`backtrack`を`([1, 1, 2], 3, 4)`で呼び出します。

6. これを繰り返していくと、最終的に`cur = [1, 1, 6]`となり、`target = 0`となります。これは解の1つとなります。

7. 過程を続けて、`cur = [1, 2, 5]`も解として得られます。

8. 同様に、`cur = [1, 7]`も解として得られます。

9. これを繰り返して、最終的な結果リスト`res = [[1, 1, 6], [1, 2, 5], [1, 7]]`が得られます。

注意: `prev`変数は、同じ数字を連続して使用することを防ぐために使われます。この例では、`candidates`の中に1が2回登場していますが、`combinationSum2`関数はこの2つの1を区別して扱います。従って、[1, 1, 6]という組み合わせが得られます。
"""