from typing import List
import collections

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    output = []
    q = collections.deque()
    l = r = 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums, k))

"""
このアルゴリズムは、配列 `nums` の中で、サイズ `k` のスライディングウィンドウが取りうる位置ごとの最大値を計算するものです。結果は `output` というリストに格納されます。

大まかな説明:
このアルゴリズムでは、ダブルエンドキュー `q` を用いて、ウィンドウ内の最大値のインデックスを保持します。`l` と `r` は、ウィンドウの左端と右端を示すポインターとして機能します。ループを通じて、`q` を常に整理して、最前面にウィンドウ内の最大値のインデックスがあるように保ちます。

詳細な説明:
部分ごとに説明していきます。

```python
output = []
```
- ここでは、結果を保存するためのリストを作成しています。このリストには、スライディングウィンドウの中での最大値を追加していきます。

```python
q = collections.deque()
```
- これは「deque」と呼ばれる特別なタイプのリストです。このリストを使用して、ウィンドウ内の数字のインデックスを追跡します。

```python
l = r = 0
```
- ここで、ウィンドウの左側(`l`)と右側(`r`)の位置を初期化しています。両方とも最初は位置`0`を指しています。

```python
while r < len(nums):
```
- `r`（ウィンドウの右側）を`nums`リストの最後まで動かしていきます。

```python
    while q and nums[q[-1]] < nums[r]:
        q.pop()
```
- もし`q`が空でなく、`q`の最後の要素（インデックスが示す数値）が現在の要素`nums[r]`より小さい場合、その要素を取り除きます。このことで、`q`の最後の要素は常に最大のものとなります。

```python
    q.append(r)
```
- `r`の位置の要素を`q`に追加します。

```python
    if l > q[0]:
        q.popleft()
```
- ウィンドウの左側が`q`の一番前の要素よりも右にある場合、その要素はウィンドウの範囲外になりますので、`q`から削除します。

```python
    if (r + 1) >= k:
        output.append(nums[q[0]])
        l += 1
```
- ウィンドウが所定のサイズ`k`に達したら、`q`の先頭の要素（これがウィンドウ内での最大値のインデックスです）を`output`に追加し、ウィンドウの左側を1つ右に移動します。

```python
    r += 1
```
- `r`を1つ右に移動させて次の要素に進みます。

```python
return output
```
- 最終的な`output`リストを返します。このリストには、各ウィンドウ内での最大値が含まれています。

このアルゴリズムは、各要素を1回だけ処理するため、O(n) の時間複雑度を持っています。
"""

"""
イメージしてほしいのは、子供たちが列を作って、お店でおもちゃを手に入れるときのような状況です。

1. **キュー**:
    - 子供たちが並んでいる列をイメージしてください。最初の子（一番前）が最も高いおもちゃを持っています。後ろの子供たちはそれよりも少し小さいおもちゃを持っていると想像してください。

2. **おもちゃを入れ替える**:
    - 新しい子供（`r`）が列に加わるとき、彼の持っているおもちゃがどれよりも大きいかを確認します。もし彼のおもちゃが他の子供のものより大きければ、他の子供たちはおもちゃを渡し、彼が最も高いおもちゃを持つことになります。彼は列に加わります。

3. **長すぎる列**:
    - しかし、列は長すぎることができません。列が一定の長さ（`k`）を超えると、最初の子供（`l`）はおもちゃとともに列を離れます。

4. **記録する**:
    - 列が十分な長さに達するたびに、最初の子供（最大のおもちゃを持つ子供）のおもちゃの高さを記録します。

---

これを繰り返すことで、最も高いおもちゃの高さを持つ子供のリストを得ることができます。このコードは、そのリストを作成しています。
"""

"""
もちろんです。指定された`nums`リストと`k`を使って、アルゴリズムをステップバイステップでシミュレーションしてみましょう。

**初期設定:**
- nums = [1,3,-1,-3,5,3,6,7]
- k = 3
- output = []
- q = deque()
- l = 0, r = 0

**シミュレーションの進行:**

1. r = 0, nums[r] = 1
   - q: deque([0])
   - output: []

2. r = 1, nums[r] = 3
   - q (before): deque([0])
   - nums[q[-1]] (= 1) < nums[r] (= 3) なので pop する。
   - q: deque([1])
   - output: []

3. r = 2, nums[r] = -1
   - q: deque([1,2])
   - output: []

4. r = 3, nums[r] = -3
   - q: deque([1,2,3])
   - 今、(r + 1) = 4 が k = 3 以上なので:
       - output に nums[q[0]] (= 3) を追加する。
       - l を1つ増やす。
   - output: [3]

5. r = 4, nums[r] = 5
   - q (before): deque([1,2,3])
   - nums[q[-1]] (= -3) < nums[r] (= 5) なので pop する。
   - nums[q[-1]] (= -1) < nums[r] (= 5) なので pop する。
   - nums[q[-1]] (= 3) < nums[r] (= 5) なので pop する。
   - q: deque([4])
   - output に nums[q[0]] (= 5) を追加する。
   - l を1つ増やす。
   - output: [3,5]

6. r = 5, nums[r] = 3
   - q: deque([4,5])
   - output に nums[q[0]] (= 5) を追加する。
   - l を1つ増やす。
   - output: [3,5,5]

7. r = 6, nums[r] = 6
   - q (before): deque([4,5])
   - nums[q[-1]] (= 3) < nums[r] (= 6) なので pop する。
   - nums[q[-1]] (= 5) < nums[r] (= 6) なので pop する。
   - q: deque([6])
   - output に nums[q[0]] (= 6) を追加する。
   - l を1つ増やす。
   - output: [3,5,5,6]

8. r = 7, nums[r] = 7
   - q (before): deque([6])
   - nums[q[-1]] (= 6) < nums[r] (= 7) なので pop する。
   - q: deque([7])
   - output に nums[q[0]] (= 7) を追加する。
   - l を1つ増やす。
   - output: [3,5,5,6,7]

このシミュレーションの結果、output は [3,5,5,6,7] となります。
"""