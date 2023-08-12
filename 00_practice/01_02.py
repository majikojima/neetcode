def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    constS, constT = {}, {}

    for i in range(len(s)):
        constS[s[i]] = 1 + constS.get(s[i], 0)
        constT[t[i]] = 1 + constT.get(t[i], 0)
        print(f"constS: {constS}")
        print(f"constT: {constT}")
    return constS == constT

s = "anagram"
t = "nagaram"

print(isAnagram(s, t))