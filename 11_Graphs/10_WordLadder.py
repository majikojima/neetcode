from typing import List
import collections

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    nei = collections.defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1 :]
            nei[pattern].append(word)

    visit = set([beginWord])
    q = collections.deque([beginWord])
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                for neiWord in nei[pattern]:
                    if neiWord not in visit:
                        visit.add(neiWord)
                        q.append(neiWord)
        res += 1
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))

"""
このコードは、単語の変換の問題で使用されます。具体的には、与えられた2つの単語`beginWord`と`endWord`、および単語のリスト`wordList`が与えられた場合、`beginWord`から`endWord`に変換するのに必要な最小の変換ステップを求めることを目的としています。ただし、1つの変換ステップでは1つの文字だけを変更できます。そして、変更後の単語は`wordList`の中に存在しなければなりません。

コードの大まかな流れと部分ごとの説明は以下の通りです。

1. **初期チェック**:
   ```python
   if endWord not in wordList:
       return 0
   ```
   まず、`endWord`が`wordList`の中に存在しない場合、変換は不可能なので0を返します。

2. **パターン生成と辞書作成**:
   ```python
   nei = collections.defaultdict(list)
   wordList.append(beginWord)
   for word in wordList:
       for j in range(len(word)):
           pattern = word[:j] + "*" + word[j + 1 :]
           nei[pattern].append(word)
   ```
   各単語に対して、その単語の各位置の文字を'*'に置き換えることでパターンを生成します。このパターンは、その位置の文字以外が同じ単語をグルーピングするのに役立ちます。

3. **BFSの初期化**:
   ```python
   visit = set([beginWord])
   q = deque([beginWord])
   res = 1
   ```
   `visit`は訪問済みの単語を記録するためのセット、`q`はBFSのキュー、そして`res`は変換のステップ数を記録します。

4. **BFSループ**:
   ```python
   while q:
       for i in range(len(q)):
           word = q.popleft()
           if word == endWord:
               return res
           for j in range(len(word)):
               pattern = word[:j] + "*" + word[j + 1 :]
               for neiWord in nei[pattern]:
                   if neiWord not in visit:
                       visit.add(neiWord)
                       q.append(neiWord)
       res += 1
   ```
   これは幅優先探索(BFS)のループです。`beginWord`から始めて、変換可能な単語を探索し続け、`endWord`に到達するまで探索を続けます。

5. **変換不可能の場合**:
   ```python
   return 0
   ```
   BFSループが完了しても`endWord`に到達しなかった場合、変換は不可能なので0を返します。
"""