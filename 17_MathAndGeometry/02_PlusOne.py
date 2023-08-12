from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print("")
        print(digits)
        one = 1
        i = 0
        digits = digits[::-1]
        while one:
            print(digits)
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        
        return digits[::-1]


s = Solution()
n = [1,2,3]
result = s.plusOne(n)
print(result)

n = [9,9,9]
result = s.plusOne(n)
print(result)

"""
この関数は、リスト形式の数字に1を加算する役割を果たします。関数の中で何が行われているかを行ごとに解説します。

1. `def plusOne(self, digits: List[int]) -> List[int]:`: `plusOne`という関数を定義します。この関数は、整数のリスト`digits`を引数に取り、整数のリストを返します。

2. `one = 1`: 加算する1の値を変数`one`に保存します。

3. `i = 0`: 現在のインデックスを追跡するためのカウンタ`i`を0で初期化します。

4. `digits = digits[::-1]`: リスト`digits`を反転させて、右から左へと操作するようにします。これにより、実際には1を加算するのが容易になります（一般的に、加算操作は右から左へ行われます）。

5. `while one:`: 1が加算されている限りループを続けます。

6. `if i < len(digits):`: 現在のインデックスがリストの長さよりも小さい場合、つまり、まだリスト内に処理すべき要素が存在する場合に次の操作を行います。

7. `if digits[i] == 9:`: 現在の要素が9の場合（1を加算すると10になり桁上がりが発生する場合）は、その位置を0にリセットします。

8. `else:`: 現在の要素が9でない場合は、その要素に1を加え、`one`を0に設定します（これにより、ループが終了します）。

9. `else:`: もし、全ての要素が9であるために、リストの終端に達した場合、リストの最後に`one`を追加し（新たな最高位の1を作成し）、`one`を0に設定します。

10. `i += 1`: インデックスカウンタを増分します。

11. `return digits[::-1]`: 加算が終了したので、リストを再度反転させ、元の順序に戻します。そして、その結果を返します。
"""

"""
このようなアルゴリズムを設計するためには、以下のようなステップを踏むことが一般的です：

1. **問題理解**: 問題の全ての側面を理解し、どのような結果が求められているのかを明確にします。この例では、リストに格納された数値に1を加えることが目的となります。

2. **問題分解**: 問題を小さな部分に分解し、個々の部分がどのように解決可能であるかを見ます。この例では、最初にリストを反転させ、次に各桁に1を追加し、必要に応じて繰り上がりを処理するという手順が必要です。

3. **アルゴリズム設計**: 問題を解決するための手順（アルゴリズム）を設計します。このステップでは、ループ、条件分岐、変数の使用など、必要なプログラミング概念を利用してアルゴリズムを設計します。

4. **コーディング**: 設計したアルゴリズムをコードに変換します。

5. **テストとデバッグ**: コードをテストして動作を確認し、問題があれば修正（デバッグ）します。

このプロセスを通じて、基本的なプログラミングスキルや、問題解決スキルを磨くことができます。また、より高度なアルゴリズムを理解し設計するためには、データ構造やアルゴリズムについての深い理解が求められます。これらはコンピューターサイエンスのカリキュラムや専門書籍、オンラインコースを通じて学ぶことができます。
"""