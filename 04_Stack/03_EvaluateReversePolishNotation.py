from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []

    for c in tokens:
        if c == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif c == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif c == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif c == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))
    return stack[0]
 
tokens = ["2","1","+","3","*","5","/"]
print(evalRPN(tokens))

"""
このコードは、逆ポーランド記法 (Reverse Polish Notation, RPN) または逆ポーランド記法としても知られる計算手法を評価する関数です。RPNは二項演算子をオペランドの後に置く記法で、計算機科学における特定のシチュエーションで有用です。

**大まかな説明**:
関数`evalRPN`は逆ポーランド記法のトークンを受け取り、その計算結果を返します。スタックを使用して、トークンが数値の場合はその数値をスタックにプッシュし、トークンが演算子の場合は必要な数のオペランドをスタックからポップして計算を行い、結果を再びスタックにプッシュします。

**部分毎の説明**:
1. `stack = []`: この行は空のリストをスタックとして初期化します。

2. `for c in tokens:`: `tokens`の各要素に対してループを開始します。

3. `if c == "+":` と以下のブロック: この部分は、現在のトークン`c`が"+"である場合、スタックの上2つの要素をポップして加算し、結果をスタックにプッシュします。

4. `elif c == "-":` と以下のブロック: `-` 演算子の場合、上2つの要素をスタックからポップし、差を計算して結果をスタックにプッシュします。ここで注意が必要なのは、順序です。最初にポップしたものが`a`で、次にポップしたものが`b`なので、`b - a`となります。

5. `elif c == "*":` と以下のブロック: `*` 演算子の場合、上2つの要素をポップして掛け算し、結果をスタックにプッシュします。

6. `elif c == "/":` と以下のブロック: `/` 演算子の場合も、順序に注意が必要です。結果は`b / a`として計算され、整数としてスタックにプッシュされます。このコードでは、除算の結果が浮動小数点数になる場合でも整数部分だけを取得するために`int()`関数が使用されています。

7. `else:`: この部分は、トークン`c`が演算子でない場合、つまり数値の場合です。その数値を整数として解析し、スタックにプッシュします。

8. `return stack[0]`: すべてのトークンの処理が終わった後、スタックの上には計算結果のみが残っています。その結果を返します。

この関数を使用すると、逆ポーランド記法で表された数式を評価することができます。
"""

"""
`tokens = ["2", "1", "+", "3", "*", "5", "/"]` を逆ポーランド記法 (RPN) で評価するシミュレーションを行います。

以下が各ステップの詳細です：

1. スタックを初期化: `stack = []`
2. `tokens`の各要素を順に評価

- `2`: 数字なのでスタックに追加。`stack = [2]`
- `1`: 数字なのでスタックに追加。`stack = [2, 1]`
- `+`: 加算演算子なのでスタックから上の2つの数字を取り出して加算。`2 + 1 = 3`。結果をスタックに追加。`stack = [3]`
- `3`: 数字なのでスタックに追加。`stack = [3, 3]`
- `*`: 乗算演算子なのでスタックから上の2つの数字を取り出して乗算。`3 * 3 = 9`。結果をスタックに追加。`stack = [9]`
- `5`: 数字なのでスタックに追加。`stack = [9, 5]`
- `/`: 除算演算子なのでスタックから上の2つの数字を取り出して除算。`9 ÷ 5 = 1.8`。ただし、以前のコードの挙動に従って結果を整数に変換すると`1`となります。結果をスタックに追加。`stack = [1]`

シミュレーションが完了した時点でのスタックの状態は `stack = [1]` です。

したがって、`tokens = ["2","1","+","3","*","5","/"]` の逆ポーランド記法の評価結果は `1` です。
"""