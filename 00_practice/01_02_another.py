from collections import Counter

def isAnagram_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def isAnagram_Counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

def isAnagram_ascii(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    count = [0] * 26

    for c in s:
        count[ord(c) - ord('a')] += 1

    for c in t:
        count[ord(c) - ord('a')] -= 1
        if count[ord(c) - ord('a')] < 0:
            return False
        
    return True

s = "anagram"
t = "nagaram"
print("sort:\n", isAnagram_sort(s, t))
print("Counter:\n", isAnagram_Counter(s, t))
print("alpha:\n", isAnagram_ascii(s, t))

s = "aaa"
t = "bbb"
print("sort:\n", isAnagram_sort(s, t))
print("Counter:\n", isAnagram_Counter(s, t))
print("alpha:\n", isAnagram_ascii(s, t))