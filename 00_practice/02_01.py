
def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not alphanum(s[l]):
            l += 1
        while l < r and not alphanum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        print(f"left: {s[l]}, right: {s[r]}")
        l += 1
        r -= 1
    return True

def alphanum(c):
    return (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    )

s = "A man, a plan, a canal: Panama"
result = isPalindrome(s)
print(result)