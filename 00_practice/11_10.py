from typing import List
import collections

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))