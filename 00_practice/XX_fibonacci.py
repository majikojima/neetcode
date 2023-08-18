def x_fibonacci(X, T):
    sequence = [0] * (X - 1) + [1]
    
    while len(sequence) < T + X - 1:
        sequence.append(sum(sequence[-X:]))
    
    # Return the first T non-zero terms
    return sequence[X-1:X-1+T]

# Input
X = int(input())
T = int(input())

# Calculate
result = x_fibonacci(X, T)

# Output
print(" ".join(map(str, result)))

"""
了解しました。関数`x_fibonacci`を説明します。

### 1. 関数の目的:
この関数は、X-Fibonacci数列の最初のT項を計算して返します。

### 2. コードの説明:

#### 2.1 `sequence = [0] * (X - 1) + [1]`
- X-Fibonacci数列を初期化します。最初に、`X-1`の0のリストと、その後に1の値を持つリストを作成します。
- 例：X=3（Tribonacci）の場合、初期数列は`[0, 0, 1]`です。

#### 2.2 `while len(sequence) < T + X - 1:`
- このループは、我々が必要とするT項が完成するまで続けられます。
- なぜ`T + X - 1`かというと、最初の`X-1`項は0であり、これらの0はカウントされないため、T項を得るためには、実際には`T + X - 1`項が必要です。

#### 2.3 `sequence.append(sum(sequence[-X:]))`
- 新しい項を計算して数列に追加します。この新しい項は、数列の最後のX項の合計です。`sequence[-X:]`は、リストの最後のX項を取得するためのスライスです。

#### 2.4 `return sequence[X-1:X-1+T]`
- 最初のT個の非ゼロの項を返します。
- `[X-1:X-1+T]`のスライスは、最初の`X-1`個の0をスキップし、それ以降のT項を取得するためのものです。

### 例:

X=3, T=4の場合:

- sequenceの初期値: `[0, 0, 1]`
- 最初のループ: `[0, 0, 1, 1]` (最後の3項の合計：0+0+1=1)
- 次のループ: `[0, 0, 1, 1, 2]` (最後の3項の合計：0+1+1=2)
- 次のループ: `[0, 0, 1, 1, 2, 4]` (最後の3項の合計：1+1+2=4)
- T=4の非ゼロの項を取得するための結果: `[1, 1, 2, 4]`

この関数は、Xというパラメータに基づいてX-Fibonacci数列を効率的に計算するためのものです。
"""