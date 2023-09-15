import math

class Solution:
    def reverse(self, x: int) -> int:
        # Integer.MAX_VALUE = 2147483647 (end with 7)
        # Integer.MIN_VALUE = -2147483648 (end with -8 )

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))  # (python dumb) -1 %  10 = 9
            x = int(x / 10)  # (python dumb) -1 // 10 = -1

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res

S = Solution()
x = 123
print(S.reverse(x))

x = -123
print(S.reverse(x))

x = 120
print(S.reverse(x))

x = 1534236469
print(S.reverse(x))

"""
このコードは、整数`x`を入力として受け取り、その整数の桁を逆にして返す関数`reverse`を定義しています。ただし、反転した結果が32ビットの整数の範囲を超えた場合は0を返します。

大まかな説明:
与えられた整数`x`の桁を逆にし、結果が32ビットの整数の範囲内に収まるかどうかを確認します。範囲を超える場合は、0を返します。

部分毎の説明:

1. `MIN` と `MAX`:
   - これは32ビット整数の最小値と最大値を示します。それぞれ、-2^31と2^31 - 1です。

2. `res = 0`:
   - `res`は、`x`の桁を逆にした結果を格納する変数です。

3. `while x:`:
   - `x`が0になるまでループを続けます。

4. `digit = int(math.fmod(x, 10))`:
   - `x`の最後の桁を取得します。Pythonの通常のモジュロ演算子`%`は、負の数に対して予期せぬ結果を返す可能性があるため、`math.fmod`を使用しています。

5. `x = int(x / 10)`:
   - `x`を10で除算して、最後の桁を削除します。この操作により、次のループイテレーションで次の桁を処理できます。

6. 次の2つのif文:
   - これらは、逆転した整数が32ビットの範囲を超えるかどうかを確認します。超える場合、関数は0を返します。

7. `res = (res * 10) + digit`:
   - `res`に新しい桁を追加します。最初は`res`は0なので、最初の桁がそのまま追加されます。次のループイテレーションでは、前回の`res`を10倍して次の桁を追加します。

8. `return res`:
   - 桁を逆にした結果を返します。

この関数は、整数の桁を逆にすることや、オーバーフローを避けるための条件を確認することにより、ビット演算と算術演算の組み合わせの理解を深めるのに役立ちます。
"""

"""
実際、両方のコードは整数を逆にする機能を持っていますが、実装の違いがあります。

1. **模範解答の方**:
    - `while`ループの中で、`res`が整数範囲を超えるかどうかを都度チェックしています。これにより、`res`が範囲を超えた瞬間に0を返して処理を終了できる利点があります。

2. **提供されたコード**:
    - `res`が範囲内に収まっているかどうかを`while`ループの後で一度だけ確認します。この方法の方がシンプルで読みやすいかもしれません。

実際の違いは、計算中に範囲外の値が出てきた場合の処理方法です。

- 模範解答の方は、範囲外の値が出たら即座に0を返します。
- 提供されたコードの方は、全ての計算が完了してから範囲のチェックを行います。

**なぜ模範解答はあんなに難しくしているか**について:

- エラーチェックを早期に行うことで、不要な計算をスキップする可能性があります。これは特に大きな入力で有利になることが考えられます。
- 安全性の観点から、計算中に範囲外の値が出る可能性を完全に排除するためには、模範解答のような途中での範囲チェックが有効です。

しかし、具体的な問題の要件や、実際に処理するデータのサイズや性質によって、どちらのアプローチが適切かは異なる場合があります。両方のアプローチにはそれぞれ利点と欠点があります。
"""