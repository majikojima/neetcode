# Greedy: O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:  # required because -> s = ( * ) (
                leftMin = 0
        return leftMin == 0
        
S = Solution()

s = "()"
print(S.checkValidString(s))

s = "(*)"
print(S.checkValidString(s))

s = "(*))"
print(S.checkValidString(s))

"""
この関数は、文字列`s`が有効な括弧の組み合わせかどうかをチェックします。ただし、`*`は、左括弧、右括弧、または空文字のいずれかとして解釈することができます。関数は、文字列が有効な場合に`True`を、そうでない場合に`False`を返します。

## 大まかな説明:
文字列`s`を検査し、それが有効な括弧の文字列かどうかを確認します。文字列内の`*`は、左括弧、右括弧、または空文字として解釈できるという点を考慮に入れます。

## 部分毎の説明:

1. `leftMin, leftMax = 0, 0`
    - `leftMin`と`leftMax`は、可能な開き括弧`(`の数の最小値と最大値を追跡するための変数です。

2. `for c in s:`
    - 文字列`s`の各文字をイテレートします。

3. `if c == "(":`
    - 現在の文字が開き括弧の場合、最小および最大のカウントをインクリメントします。

4. `elif c == ")":`
    - 現在の文字が閉じ括弧の場合、最小および最大のカウントをデクリメントします。

5. `else:`
    - 現在の文字が`*`の場合、それを左括弧、右括弧、または空文字として解釈することができます。したがって、最小カウントをデクリメントし、最大カウントをインクリメントします。

6. `if leftMax < 0:`
    - この時点で`leftMax`が0未満の場合、文字列は有効である可能性がありません。

7. `if leftMin < 0:`
    - もし`leftMin`が0未満の場合、それは`*`を右括弧として解釈することで正常化できるという意味です。したがって、`leftMin`を0にリセットします。

8. `return leftMin == 0`
    - 文字列が有効であるためには、可能な開き括弧の数の最小値が0である必要があります。

このアプローチは、可能な解釈を考慮しながら、文字列が有効な括弧の文字列であるかどうかを効率的に判断するためのものです。
"""

"""
了解しました。この部分をもう少し詳しく説明します。

まず、`leftMin`と`leftMax`は可能な開き括弧`(`の最小値と最大値を示しています。特に`*`の存在により、括弧の数には変動があるため、最小値と最大値の両方を追跡する必要があります。

`*`を見たとき、我々は3つの選択肢があることを思い出してください:
1. `*`を左括弧`(`として解釈する（これが`leftMax`を増加させる理由）
2. `*`を右括弧`)`として解釈する（これが`leftMin`を減少させる理由）
3. `*`を無視する（何もしない）

`leftMin`が0未満になった場合、これは実際には多すぎる右括弧`)`が存在することを意味します。しかし、前述の通り、`*`は右括弧として解釈することができるため、この`*`を使って過剰な右括弧を相殺することができます。

具体的には、`leftMin < 0`という状態は、必要な左括弧が足りていないことを示していますが、我々はそれを`*`を右括弧として解釈することで補うことができます。

この動作をもう少し具体的に考えてみましょう。例えば、以下の文字列を考えてみてください:
`s = "*()"`

ここで、最初の`*`を見たときに、それを左括弧として考えることも、右括弧として考えることも、無視することもできます。しかし、文字列の残りを読むと、右括弧`)`が余ってしまいます。この場合、`leftMin`が-1になります。しかし、最初の`*`を右括弧として解釈することで、この不均衡を解消することができます。

そのため、`if leftMin < 0:`の下の行で`leftMin`を0にリセットするのは、このようなケースを処理するためです。
"""

"""
"Greedy"（貪欲法）というアルゴリズムの戦略は、その名の通り、問題を解決するための選択をする際に、その時点で最も良いと思われる選択を常に取る方法を指します。このような選択は局所的な最適解を求めるもので、必ずしも最終的な全体の最適解に結びつくとは限りません。しかし、多くの問題において、貪欲法を適用することで効率的に全体の最適解または近似解を得ることができます。

例えば、上で取り上げた`checkValidString`の問題の場合、各ステップで最も良いと思われる選択（`*`を`(`、`)`、または何もしない、として扱う）をしています。このように、各ステップで最適な選択をする戦略を取るため、この問題の解決策は"greedy"と言えます。

貪欲法の利点は、実装が比較的シンプルであり、計算が高速であることです。しかし、全ての問題に対して貪欲法が最適解を導くわけではありません。問題の性質や制約によっては、他の方法（動的計画法、分割統治法など）の方が適切な場合もあります。
"""