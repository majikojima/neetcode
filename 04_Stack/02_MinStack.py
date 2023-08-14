from typing import List

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
    def getStack(self) -> List[int]:
        return self.stack
    
    def getMinStack(self) -> List[int]:
        return self.minStack

minStack = MinStack()
minStack.push(-2)
print("getStack: ", minStack.getStack())
print("getMinStack: ", minStack.getMinStack())
minStack.push(0)
print("getStack: ", minStack.getStack())
print("getMinStack: ", minStack.getMinStack())
minStack.push(-3)
print("getStack: ", minStack.getStack())
print("getMinStack: ", minStack.getMinStack())
print("getMin: ", minStack.getMin())
minStack.pop()
print("top: ", minStack.top())
print("getMin: ", minStack.getMin())
print("getStack: ", minStack.getStack())
print("getMinStack: ", minStack.getMinStack())

"""
このコードは、特定のスタックデータ構造を実装していますが、このスタックは通常のスタックに加えて、その時点でのスタックの最小値を常に追跡します。スタックの最小値を取得する操作はO(1)の時間複雑度で行われます。

## 大まかな説明:

- `stack`は通常のスタックを実装するためのもので、整数値を保持します。
- `minStack`は、`stack`の各段階での最小値を保持するためのものです。
- `push`操作は、値を`stack`に追加し、その時点での最小値を`minStack`に追加します。
- `pop`操作は、`stack`と`minStack`の両方から最後の値を取り除きます。
- `top`操作は、`stack`の最上部の値を返します。
- `getMin`操作は、現在のスタックの最小値を返します。

## 部分毎の説明:

- `__init__(self)`: 
  - 初期化関数。スタックと最小値スタックの両方を空のリストとして初期化します。

- `push(self, val: int) -> None`: 
  - `val`を`stack`に追加する関数。
  - `minStack`が空でない場合、`val`と`minStack`の最上部の値のうち、より小さい方を新しい最小値として認識します。`minStack`が空の場合、`val`が最小値となります。
  - そして、その新しい最小値を`minStack`に追加します。

- `pop(self) -> None`: 
  - 最後の要素を`stack`と`minStack`の両方から削除する関数。

- `top(self) -> int`: 
  - `stack`の最上部の要素を返す関数。

- `getMin(self) -> int`: 
  - 現在のスタックの最小値を返す関数。これは、`minStack`の最上部の値として簡単にアクセスできます。

この設計のメリットは、最小値の取得がO(1)の時間複雑度で可能であることです。一方、この設計のオーバーヘッドとして、追加のスペースが必要であるという点が挙げられます。
"""

"""
この`MinStack`クラスの実装方法によっては、`minStack`には現在の`stack`の各ステップでの最小値が含まれるので、この動作は正確です。

具体的には、次のように動作します:

1. `-2`をpush:
   - `stack`: [-2]
   - `minStack`: [-2]（-2はこの時点での最小値）

2. `0`をpush:
   - `stack`: [-2, 0]
   - `minStack`に新しい値を追加する際に、`0`と`minStack`の最後の値（`-2`）を比較します。`-2`の方が小さいので、`minStack`にも`-2`を追加します。
   - `minStack`: [-2, -2]

この実装方法の利点は、`pop`操作をするたびに、`stack`と`minStack`の両方から要素を削除するだけで、常に`minStack`のトップに現在の`stack`の最小値が格納されているので、`getMin`関数は常にO(1)の時間複雑度で最小値を返すことができるという点です。
"""