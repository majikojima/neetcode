def isValid(s: str) -> bool:
    Map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in Map:
            stack.append(c)
            # print(f"stack.append: {c}")
            continue
        if not stack:
            return False
        if stack[-1] != Map[c]:
            return False
        # print(f"stack.pop:\n{stack}")
        stack.pop()

    return True

s = "()[]{}"
print(isValid(s))

s = "(]"
print(isValid(s))

Map = {")": "(", "]": "[", "}": "{"}
print(f"Map[')']: {Map[')']}")
if "(" in Map:
    print("( in Map")
else:
    print("not ( in Map")