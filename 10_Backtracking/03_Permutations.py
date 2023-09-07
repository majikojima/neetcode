from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    res = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res

nums = [1,2,3]
print(permute(nums))

nums = [1]
print(permute(nums))

"""
了解しました。以下にコードの大まかな説明および各部分の詳細な説明を提供します。

### 大まかな説明:

この`permute`メソッドは、与えられた数値のリスト`nums`のすべての順列を返す関数です。順列とは、元のリストの要素を再配列することで得られるすべての可能なリストを指します。この関数は再帰的なアプローチを使用して順列を生成しています。

### 部分ごとの詳細な説明:

1. `res = []`: すべての順列を格納するための結果のリストを初期化します。

2. `if len(nums) == 1:`: ベースケース。`nums`の長さが1の場合、その1つの要素のみを持つリストの順列は、そのリスト自体です。
   
    - `return [nums[:]]`: `nums[:]`は`nums`のディープコピーを取るための方法です。これにより、`nums`の元の内容を変更せずにそのコピーを返すことができます。

3. `for i in range(len(nums)):`: `nums`の各要素についてループ処理を行い、その要素を固定した上で残りの要素の順列を求めます。

    - `n = nums.pop(0)`: `nums`の最初の要素を取り出し、`n`に保存します。

    - `perms = self.permute(nums)`: 残りの`nums`に対して再帰的に`permute`関数を呼び出し、`n`を除く`nums`のすべての順列を取得します。

    - `for perm in perms:`: 取得したすべての順列についてループ処理を行います。
       
        - `perm.append(n)`: 取り出した要素`n`を各順列の最後に追加します。

    - `res.extend(perms)`: 生成されたすべての順列を`res`に追加します。

    - `nums.append(n)`: `n`を`nums`の最後に戻して、次の要素を固定する準備をします。

4. `return res`: すべての順列が含まれるリスト`res`を返します。

この関数は、リストのすべての要素を1つずつ固定して、残りの要素の順列を再帰的に計算することで、与えられたリストのすべての順列を生成します。
"""

"""
分かりました。より具体的な方法でこの関数の動きを理解するために、手を動かしながらシンプルな例をトレースしてみましょう。

例として、`nums = [1, 2, 3]`という小さなリストを使用します。

1. 関数は`res = []`で結果を格納するリストを初期化します。
   
2. `nums`の長さは1より大きいので、ベースケースはスキップされます。

3. 最初のループのイテレーションでは、`n = 1`として、`1`を`nums`から取り出します。これにより、`nums`は`[2, 3]`となります。

4. 次に、`nums = [2, 3]`の順列を求めるために、`self.permute([2, 3])`が再帰的に呼び出されます。

    - この再帰呼び出しでは、最初に`2`を固定して、`[3]`の順列を求めます。これにより、順列として`[2, 3]`が得られます。
    - 次に、`3`を固定して、`[2]`の順列を求めます。これにより、順列として`[3, 2]`が得られます。

5. これらの2つの順列に、`1`を追加して、`[2, 3, 1]`および`[3, 2, 1]`の2つの順列が得られます。

6. 次に、最初のループで`n = 2`として、`2`を`nums`から取り出し、上記のプロセスを繰り返して、`1`と`3`の順列を求めます。

7. この方法で、すべての可能な順列が得られます。

関数の動きを具体的な例を使用して手を動かしながらトレースすることで、動作を理解するのが少し楽になるかもしれません。
"""