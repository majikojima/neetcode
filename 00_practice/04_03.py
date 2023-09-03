from typing import List

def evalRPN(tokens: List[str]) -> int:


tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))

tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))