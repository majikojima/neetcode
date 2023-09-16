from typing import List

def myPow(x: float, n: int) -> float:
    def helper(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = helper(x * x, n // 2)
        return x * res if n % 2 else res

    res = helper(x, abs(n))
    return res if n >= 0 else 1 / res

x = 2.00000
n = 10
print(myPow(x, n))

x = 2.10000
n = 3
print(myPow(x, n))

x = 2.00000
n = -2
print(myPow(x, n))

"""
この関数 `myPow` は、指定された数 `x` を指定された指数 `n` で累乗するものです。このアルゴリズムは、バイナリ累乗法（または「分割して統治する」アプローチ）を使用して高速に累乗を計算します。

**大まかな説明**:
1. `helper` 関数を再帰的に使用して、結果を効率的に計算します。
2. `n` が負の場合、結果を反転して返します。

**部分毎の説明**:

1. `helper` 関数の定義:
    - この関数は、再帰的に累乗を計算するための内部関数です。
    
    ```python
    def helper(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
    ```
    上記の2つの基本ケースは次のとおりです。
    - `x` が0の場合、返り値は0です。
    - `n` が0の場合、返り値は1です。

    ```python
    res = helper(x * x, n // 2)
    return x * res if n % 2 else res
    ```
    - ここでは、再帰的なアプローチを取っています。`x` を2乗し、`n` を2で割ることで、計算の効率を向上させます。
    - もし `n` が奇数なら、結果は `x` で乗算される必要があります。そうでない場合、そのままの結果を返します。

2. 主要な関数の動作:
    ```python
    res = helper(x, abs(n))
    ```
    - `helper` 関数を `n` の絶対値で呼び出して、累乗の正の部分を計算します。

    ```python
    return res if n >= 0 else 1 / res
    ```
    - 最終的に、もし `n` が負の場合、結果を反転して返します。

このアルゴリズムは、`O(log n)` の時間複雑度で累乗を計算できるため、非常に効率的です。
"""