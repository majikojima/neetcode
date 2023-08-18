from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A
    
    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2 # A
        j = half - i - 2 # B

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
        
        # partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if total % 2:
                return min(Aright, Bright)
            # even
            else:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

nums1 = [1,2,3]
nums2 = [4,5,6,7,8]
print(findMedianSortedArrays(nums1, nums2))

"""
このコードは、2つのソート済みの整数配列`nums1`と`nums2`が与えられたとき、それらをマージしたと仮定した場合の中央値を計算するものです。このアルゴリズムはバイナリサーチを活用しており、O(log(min(n, m)))の時間複雑度で動作します。

コードの大まかな説明と、部分ごとの詳細を以下に示します。

### 大まかな説明:

1. `nums1`と`nums2`の長さを考慮して、より短い配列を`A`に、長い配列を`B`に割り当てます。
2. 総数とその半分を計算します。
3. `A`の中央値を基点にしてバイナリサーチを行い、適切なパーティションを見つけます。
4. 適切なパーティションを見つけた場合、中央値または中央値の平均を返します。

### 部分毎の説明:

1. **初期設定**:
    ```python
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    ```
    ここでは、入力配列と全体の長さ、そして中央の位置を計算しています。

2. **配列の入れ替え**:
    ```python
    if len(B) < len(A):
        A, B = B, A
    ```
    `B`を常により長い配列とするためのスワップです。

3. **バイナリサーチの初期設定**:
    ```python
    l, r = 0, len(A) - 1
    ```

4. **バイナリサーチのループ**:
    ```python
    while True:
        i = (l + r) // 2  # A
        j = half - i - 2  # B
    ```
    ここで、`A`の中央を`i`として、それに対応する`B`の位置を`j`として計算しています。

5. **パーティションのエッジケースの処理**:
    ```python
    Aleft = A[i] if i >= 0 else float("-infinity")
    Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
    Bleft = B[j] if j >= 0 else float("-infinity")
    Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
    ```
    上記は、各配列のパーティションを取得するコードです。エッジケースを考慮して、配列の端に達した場合は無限大または負の無限大を代入しています。

6. **適切なパーティションのチェック**:
    ```python
    if Aleft <= Bright and Bleft <= Aright:
        ...
    ```
    適切なパーティションが見つかった場合の処理です。

7. **中央値の計算と返却**:
    配列の合計が奇数の場合と偶数の場合で中央値を計算し、返します。

8. **バイナリサーチの更新**:
    適切なパーティションを見つけるために、検索範囲を更新する部分です。

このアルゴリズムは、バイナリサーチを使用して2つのソート済み配列の中央値を効率的に計算するための方法です。
"""

"""
もちろん、これらの行について詳しく説明します。

```python
i = (l + r) // 2  # A
j = half - i - 2  # B
```

これはバイナリサーチにおける中央の計算です。ここで、`i`は配列`A`の中央を示しています。そして`j`は、`half`（`A`と`B`の要素の合計数の半分）から`i`を引いた後、さらに2を引いた数を示します。この`j`の計算は、`A`のパーティションと`B`のパーティションの間の関係を維持するためです。例えば、`A`が4つの要素を持ち、`B`が5つの要素を持つ場合、中央は4+5の半分で4.5となり、この位置を元にパーティションを計算します。

次に、各配列のパーティションのエッジケースを処理します。

```python
Aleft = A[i] if i >= 0 else float("-infinity")
Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
Bleft = B[j] if j >= 0 else float("-infinity")
Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
```

- `Aleft`: `i`が0以上であれば、`A`の`i`番目の要素を取得します。それ以外の場合、負の無限大を代入します。
- `Aright`: `i + 1`が`A`の長さ未満であれば、`A`の`i+1`番目の要素を取得します。それ以外の場合、正の無限大を代入します。
- `Bleft`: `j`が0以上であれば、`B`の`j`番目の要素を取得します。それ以外の場合、負の無限大を代入します。
- `Bright`: `j + 1`が`B`の長さ未満であれば、`B`の`j+1`番目の要素を取得します。それ以外の場合、正の無限大を代入します。

このようなエッジケースの処理は、バイナリサーチの中でパーティションが配列の端に達した場合に、比較を適切に行うために必要です。無限大と負の無限大を使用することで、任意の実数と比較したときに常に最大または最小となり、その他の条件判断をシンプルに保つことができます。
"""