def lengthOfLongestSubstring(s: str) -> int:
    res = 0
    sub = []
    l = 0
    r = 0
    while r < len(s):
        if s[r] not in sub:
            sub.append(s[r])
            r += 1
        else:
            sub.remove(s[l])
            l += 1
        res = max(res, len(sub))
    return res

s = "abcabcbb"
print(lengthOfLongestSubstring(s))

"""
はい、模範解答の方が計算量の面で優れています。その理由を説明します。

1. **あなたのコード**：
   - `if s[r] not in sub:` この操作は、最悪の場合、リスト`sub`の全ての要素を確認する必要があり、O(n)の計算量がかかる可能性があります。
   - `sub.append(s[r])` この操作はO(1)の計算量です。
   - `sub.remove(s[l])` この操作は最悪の場合、リスト`sub`の全ての要素をシフトする必要があるため、O(n)の計算量がかかる可能性があります。

   したがって、あなたのコードの計算量は最悪の場合O(n^2)になります。

2. **模範解答**：
   - `while s[r] in charSet:` および `charSet.add(s[r])` これらの操作は、セットを使用しているため、平均的な場合にはO(1)の計算量で実行できます。
   - `charSet.remove(s[l])` この操作もO(1)の計算量です。

   したがって、模範解答の計算量はO(n)です。

**結論**：  
リストを使用すると、要素の存在確認や削除にO(n)の計算量がかかる可能性があるのに対して、セットを使用すると、これらの操作がO(1)の計算量で行えます。このため、模範解答の方が計算量の面で優れています。
"""