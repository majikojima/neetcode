from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:

s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s, wordDict))

s = "applepenapple"
wordDict = ["apple","pen"]
print(wordBreak(s, wordDict))

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(wordBreak(s, wordDict))