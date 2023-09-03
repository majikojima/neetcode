from typing import List

class MinStack:
    def __init__(self):


    def push(self, val: int) -> None:

    def pop(self) -> None:

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
print("top:\t",minStack.top())
print("getMin:\t",minStack.getMin())
minStack.push(0)
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())
print("top:\t",minStack.top())
print("getMin:\t",minStack.getMin())
minStack.push(-3)
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())
print("top:\t",minStack.top())
print("getMin:\t",minStack.getMin())
minStack.pop()
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())
print("top:\t",minStack.top())
print("getMin:\t",minStack.getMin())
minStack.pop()
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())
print("top:\t",minStack.top())
print("getMin:\t",minStack.getMin())
minStack.pop()


minStack.push(2)
minStack.push(0)
minStack.push(3)
minStack.push(0)
print("getStack:\t", minStack.getStack())
print("getMinStack:\t", minStack.getMinStack())