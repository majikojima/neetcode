from typing import List

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
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
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())
minStack.push(0)
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())