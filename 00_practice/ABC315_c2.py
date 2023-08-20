# [https://atcoder.jp/contests/abc315/tasks/abc315_c]
N = int(input())
F, S = [], []
maxS, choice = 0, -1
for i in range(N):
    f, s = map(int, input().split())
    if s > maxS:
        maxS = s
        choice = i
    F.append(f)
    S.append(s)
ans = 0
for i in range(N):
    if i != choice:
        if F[i] == F[choice]:
            t = maxS + (S[i] // 2)
        else:
            t = maxS + S[i]
        ans = max(ans, t)
print(ans)

"""
まず、コード全体の大まかな説明から始めます。

### 大まかな説明
このコードは、入力として複数のペア (f, s) を受け取り、それぞれのペアに基づいて特定の計算を行い、最終的な結果を求めるものです。コードは、最大の`s`の値を持つペアを特定し、そのペアと他の全てのペアの間の特定の計算を実施して、求めた結果の中の最大値を出力します。

### 部分毎の説明

1. `N = int(input())`
   - ユーザーからの入力を受け取り、それを整数として`N`に格納します。これはペアの数を表しています。

2. `F, S = [], []`
   - FとSという2つの空のリストを初期化します。これらは後で値`f`と`s`を格納するためのリストとなります。

3. `maxS, choice = 0, -1`
   - `maxS`は最大の`s`の値を格納するための変数、`choice`は最大の`s`の値を持つペアのインデックスを格納するための変数です。

4. forループによる入力と最大sのペアの特定:
   - `f, s = map(int, input().split())`でユーザーから2つの整数を受け取ります。
   - その後、もし`s`がこれまでの最大値`maxS`よりも大きければ、`maxS`と`choice`を更新します。
   - 各ペアの`f`と`s`の値をそれぞれのリスト`F`と`S`に追加します。

5. `ans = 0`
   - 最終的な答えを格納する変数`ans`を初期化します。

6. forループによる計算:
   - すべてのペアをループで回り、特定の計算を行います。ただし、最大の`s`の値を持つペアは除外されます。
   - 計算内容は、最大の`s`の値に、現在のペアの`s`の値を特定の方法で割ったものを足すというものです。その割る値は、`F`の値が最大の`s`を持つペアの`F`の値と同じかどうかによって決まります。

7. `print(ans)`
   - 最後に、求められた結果の最大値を出力します。

このコードは、入力として与えられたペアの情報に基づいて特定の計算を行い、その結果の最大値を出力するものとなっています。
"""