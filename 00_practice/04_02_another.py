from typing import List

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

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
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())
minStack.push(-2)
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())
minStack.push(0)
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())
minStack.pop()
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())
minStack.pop()
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())
minStack.pop()
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())

"""
### 方法2: `minStack`に現在の最小値だけを格納する

この方法では、`minStack`に現在の最小値だけを格納します。具体的には、新しい要素が現在の最小値以下の場合にのみ`minStack`に追加します。これにより、`minStack`のサイズは元のスタックのサイズよりも小さくなる可能性があります。

この実装方法の特徴は次のとおりです：
- `push`の際、新しい要素が現在の最小値以下の場合にのみ`minStack`に追加します。
- `pop`の際、`stack`のトップ要素が現在の最小値と同じ場合、その最小値を`minStack`からも削除します。これは、その最小値が`stack`から消えた後、次の最小値が`minStack`の新しいトップになるためです。

この方法も、`getMin`はO(1)の時間複雑度で最小値を返すことができます。
"""