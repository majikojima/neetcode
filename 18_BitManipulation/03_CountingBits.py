from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

s = Solution()
n = 5
result = s.countBits(n)
print(result)

"""
このコードは、0から`n`までの整数それぞれについて、その2進数表現に含まれる1の数を求めるものです。これは「ビットカウント」問題としてよく知られています。

- `dp = [0] * (n + 1)`: `n+1`の長さを持つリストを作成し、すべての要素を0に初期化します。このリスト（dpリスト）は、整数`i`のビット表現に含まれる1の数を記録します。リストのインデックスがその数を表し、その値が1の数です。

- `offset = 1`: offset変数は、1のビットが最後に現れた位置を追跡します。

- `for i in range(1, n + 1)`: このループは、1から`n`までのすべての数について実行されます。

  - `if offset * 2 == i:`: offsetを2倍した値が現在の数`i`と等しい場合、これは現在の数が2のべき乗であることを意味します。2のべき乗の場合、1のビットは最左位（インデックス0）にのみ存在し、他のすべてのビットは0です。

    - `offset = i:`: その場合、offsetを現在の数`i`に更新します。これにより、次の数の計算でこの位置を使用できます。

  - `dp[i] = 1 + dp[i - offset]`: 現在の数`i`のビット表現に含まれる1の数を計算します。これは、前の「offset」までの数の1の数に1（現在のビット）を加えたものです。

- 最後に、計算結果であるdpリストを返します。このリストの各インデックス`i`の値は、その数（`i`）の2進数表現に含まれる1の数です。
"""

"""
分かりました！もう少し簡単な言葉で説明しますね。

このコードは、0からnまでの各数字について、「その数字を二進数にしたときに何個の1が含まれるか」を数えるためのものです。

もし、自分が数字のリストを持っていて、リストの中の各数字が何個の1を含んでいるかを数えたいとしたら、どうしますか？

ひとつの方法は、各数字をひとつひとつ見て、それぞれの数字について1が何個あるかを数えることですね。でもこれだと時間がかかりますよね。

だから、もっと早くできる方法を考えました。前に数えた結果を覚えておいて、それを次の数字にも使います。それが「dp」というリストです。そして、「offset」というものを使って、どの数字の結果を次に使うべきかを知ります。

具体的には、次のようになります：

1. 最初に、0からnまでの数値のために「dp」という名前のリストを作ります。最初はすべての場所に0を入れます。

2. 次に、「offset」というものを1に設定します。

3. そして、数字1からnまで順番に見ていきます。

   - もし「offset」の2倍が今見ている数字と同じだったら、「offset」をその数字に変えます。

   - 次に、"dp"の今見ている数字の場所に「1 + "dp"の（今見ている数字 - "offset"）の場所の数」を書きます。これは「今見ている数字には少なくとも1つの1が含まれているはずだから、それに"dp"の（今見ている数字 - "offset"）の場所に書かれている1の数を足す」という意味です。

4. 最後に、"dp"というリストを返します。

こうすると、各数字が二進数で何個の1を含んでいるかを素早く見つけることができます。
"""

"""
このステートメントの背後にあるロジックを理解するために、いくつかの具体的な例を考えてみましょう。

まず、`offset`の意味を再確認しましょう。`offset`は、現在の数`i`の2進数表現の中で最も右にある1の位置（または、前回の2のべき乗の値）を指します。

以下に、このロジックがどのように機能するかの例を示します。

1. i = 5 の場合:
   - 5の2進数表現: 101
   - offset = 4 (これは前回の2のべき乗である)
   - 5 - offset = 1 (2進数で: 1)
   - iの最も右の0を1にすると、5になることがわかります。
   - したがって、5の1の数 = 1 (i - offsetの1の数) + 1 = 2

2. i = 6 の場合:
   - 6の2進数表現: 110
   - offset = 4
   - 6 - offset = 2 (2進数で: 10)
   - iの最も右の0を1にすると、6になることがわかります。
   - したがって、6の1の数 = 1 (i - offsetの1の数) + 1 = 2

この例からわかるように、`i - offset`の1の数に1を足すことで、新しい数`i`の1の数を効率的に計算することができます。

このロジックは、ある数が2のべき乗とその前の2のべき乗の間の数である場合にのみ適用されることに注意してください。
"""