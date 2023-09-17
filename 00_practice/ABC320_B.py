# [https://atcoder.jp/contests/abc320/tasks/abc320_b]

def longestPalindrome(s: str) -> int:
    maxLength = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if isPalindrome(s[i:j]):
                maxLength = max(maxLength, j - i)
    return maxLength

def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

S = input()
print(longestPalindrome(S))