class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrom(s[i:j+1]):
                    res.append(s[i:j+1])
        return res

    def isPalindrom(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

S = Solution()
s = "abc"
print(S.countSubstrings(s))

s = "aaa"
print(S.countSubstrings(s))