# Greedy: O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        
S = Solution()

s = "()"
print(S.checkValidString(s))

s = "(*)"
print(S.checkValidString(s))

s = "(*))"
print(S.checkValidString(s))