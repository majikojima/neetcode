from typing import List

def multiply(num1: str, num2: str) -> str:
    if "0" in [num1, num2]:
        return "0"

    res = [0] * (len(num1) + len(num2))
    num1, num2 = num1[::-1], num2[::-1]
    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            digit = int(num1[i1]) * int(num2[i2])
            res[i1 + i2] += digit
            res[i1 + i2 + 1] += res[i1 + i2] // 10
            res[i1 + i2] = res[i1 + i2] % 10

    res, beg = res[::-1], 0
    while beg < len(res) and res[beg] == 0:
        beg += 1
    res = map(str, res[beg:])
    return "".join(res)

num1 = "2"
num2 = "3"
print(multiply(num1, num2))

num1 = "123"
num2 = "456"
print(multiply(num1, num2))

"""
この関数 `multiply` は、2つの非負の整数の文字列を取得して、それらの乗算の結果を文字列として返します。このアルゴリズムは、学校の乗算法（各桁を掛け合わせてキャリーを次の桁に持ち越す方法）を使って、各桁ごとに乗算を行います。

**大まかな説明**:
1. どちらかの数が "0" の場合、結果は "0" です。
2. それぞれの桁ごとに乗算を行い、結果を格納するためのリストを準備します。
3. 最後に、結果を逆順にして、先頭の不要な0を削除して返します。

**部分毎の説明**:

1. ゼロチェック:
    ```python
    if "0" in [num1, num2]:
        return "0"
    ```
    - どちらかの数が0の場合、乗算の結果は0です。

2. 結果の格納先を準備:
    ```python
    res = [0] * (len(num1) + len(num2))
    ```
    - 最大の長さの結果は、2つの数の長さの合計と等しい可能性があります。

3. 数字を逆順にして、低位から高位への計算を容易にします:
    ```python
    num1, num2 = num1[::-1], num2[::-1]
    ```

4. 各桁ごとの乗算:
    ```python
    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            digit = int(num1[i1]) * int(num2[i2])
            res[i1 + i2] += digit
            res[i1 + i2 + 1] += res[i1 + i2] // 10
            res[i1 + i2] = res[i1 + i2] % 10
    ```
    - 各桁を乗算し、その結果を `res` の適切な位置に加算します。
    - キャリーを次の桁に持ち越します。

5. 結果を正しい順序にして、先頭の0を削除:
    ```python
    res, beg = res[::-1], 0
    while beg < len(res) and res[beg] == 0:
        beg += 1
    res = map(str, res[beg:])
    return "".join(res)
    ```
    - `res` を逆順にし、先頭の不要な0をスキップします。
    - 最後に、整数のリストを文字列のリストに変換し、結果を返します。

この関数は、2つの数の各桁ごとの乗算を行うため、時間の複雑さは \(O(n \times m)\) です（ここで、\(n\) は `num1` の長さ、\(m\) は `num2` の長さです）。
"""