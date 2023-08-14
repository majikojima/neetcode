def isValid(s: str) -> bool:
    stack = []
    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        else:
            if not stack:
                return False
            if c == ')' and stack[-1] != '(':
                return False
            if c == ']' and stack[-1] != '[':
                return False
            if c == '}' and stack[-1] != '{':
                return False
            stack.pop()
    return not stack
    
s = "()[]{}"
print(isValid(s))

s = "(]"
print(isValid(s))