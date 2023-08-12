# [https://leetcode.com/problems/valid-palindrome/]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def alphanum(self, c) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
    
s = Solution()
st = "A man, a plan, a canal: Panama"
result = s.isPalindrome(st)
print(result)

"""
このコードは、与えられた文字列がパリンドローム（前から読んでも後ろから読んでも同じになる単語やフレーズ）であるかどうかを判断します。パリンドロームの判断では大文字・小文字の違いは無視され、またアルファベットや数字以外の文字も無視します。

コードの行ごとの説明は次のとおりです：

1. `class Solution:`: Solutionという名前のクラスを定義します。

2. `def isPalindrome(self, s: str) -> bool:`: isPalindromeというメソッドを定義します。このメソッドは文字列sを引数とし、ブール値を返します。

3. `l, r = 0, len(s) - 1`: 文字列の最初と最後の文字のインデックスを指す二つのポインタを初期化します。

4. `while l < r:`: lがrより小さい間（つまり、左右のポインタが交差しない間）、次の処理を行います。

5. `while l < r and not self.alphanum(s[l]):`: 左のポインタが右のポインタより小さく、かつ、左のポインタが指す文字がアルファベットまたは数字でない間、次の処理を行います。

6. `l += 1`: 左のポインタを右に一つ移動します。

7. `while l < r and not self.alphanum(s[r]):`: 右のポインタが左のポインタより大きく、かつ、右のポインタが指す文字がアルファベットまたは数字でない間、次の処理を行います。

8. `r -= 1`: 右のポインタを左に一つ移動します。

9. `if s[l].lower() != s[r].lower():`: 左右のポインタが指す文字（小文字に変換した場合）が異なるなら、文字列はパリンドロームではないと判断し、Falseを返します。

10. `l += 1, r -= 1`: 左のポインタは右に一つ移動し、右のポインタは左に一つ移動します。

11. `return True`: 文字列全体を調べてパリンドロームでないと判断されなかった場合、文字列はパリンドロームであると判断し、Trueを返します。

13. `def alphanum(self, c):`: alphanumというメソッドを定義します。このメソッドは文字cを引数に取り、その文字がアルファベットまたは数字ならTrueを、そうでなければFalseを返します。

14-16. `return (...`: 与えられた文字が大文字のアルファベット、小文字のアルファベット、または数字であればTrueを、そうでなければFalseを返します。

このようにして、このコードはアルファベットと数字だけを考慮に入れ、大文字と小文字の違いを無視して、文字列がパリンドロームであるかどうかを判断します。
"""