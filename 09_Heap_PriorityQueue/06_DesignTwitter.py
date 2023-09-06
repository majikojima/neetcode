from collections import defaultdict
from typing import List
import heapq

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(userId=1,tweetId=1)
obj.postTweet(userId=1,tweetId=2)
obj.postTweet(userId=1,tweetId=3)
obj.postTweet(userId=1,tweetId=4)
obj.postTweet(userId=1,tweetId=5)
print(obj.getNewsFeed(userId=1))
obj.follow(followerId=1,followeeId=2)
obj.follow(followerId=1,followeeId=3)
obj.postTweet(userId=2,tweetId=6)
obj.postTweet(userId=3,tweetId=7)
obj.postTweet(userId=2,tweetId=8)
obj.postTweet(userId=3,tweetId=9)
obj.postTweet(userId=1,tweetId=10)
obj.postTweet(userId=1,tweetId=11)
print(obj.getNewsFeed(userId=1))
obj.unfollow(followerId=1,followeeId=2)
print(obj.getNewsFeed(userId=1))
print(obj.getNewsFeed(userId=2))
print(obj.getNewsFeed(userId=3))

"""
このコードは、ユーザーがツイートを投稿したり、他のユーザーをフォロー/アンフォローしたり、最新のツイートのフィードを取得したりするシンプルな「Twitter」システムをシミュレートするものです。

大まかな説明:
`Twitter`クラスは、ユーザーごとのツイートのリストとフォロー関係を追跡するためのデータ構造を保持しています。ユーザーはツイートを投稿でき、他のユーザーをフォロー/アンフォローでき、最新の10件のツイートを取得するための`getNewsFeed`メソッドも提供されています。

部分毎の説明:

1. `__init__(self):`  
このメソッドは、新しい`Twitter`オブジェクトの初期化を担当します。
    - `self.count`は、ツイートの一意性と時系列順序を保つためのカウンターです。
    - `self.tweetMap`は、ユーザーIDをキーとして、そのユーザーが投稿したツイートのリストを値とする辞書です。
    - `self.followMap`は、ユーザーIDをキーとして、そのユーザーがフォローしているユーザーのIDのセットを値とする辞書です。

2. `postTweet(self, userId: int, tweetId: int):`  
このメソッドは、指定されたユーザーIDのユーザーが新しいツイートを投稿するのをシミュレートします。

3. `getNewsFeed(self, userId: int):`  
このメソッドは、指定されたユーザーのニュースフィードの最新10件のツイートを取得します。ここではミニマムヒープを使用して、最も新しいツイートを効率的に取得します。

4. `follow(self, followerId: int, followeeId: int):`  
このメソッドは、`followerId`のユーザーが`followeeId`のユーザーをフォローするのをシミュレートします。

5. `unfollow(self, followerId: int, followeeId: int):`  
このメソッドは、`followerId`のユーザーが`followeeId`のユーザーのフォローを解除するのをシミュレートします。

この実装は、指定されたAPIの要件を効率的に満たすためのものであり、特定のタスクに対して最適化されています。
"""

"""
了解しました。以下にコードの大まかな説明および各部分の詳細な説明を提供します。

### 大まかな説明:

この`getNewsFeed`メソッドは、指定されたユーザー(`userId`)のニュースフィードに表示されるツイートのIDのリストを返します。ニュースフィードは、ユーザー自身と彼がフォローしているユーザーが投稿したツイートのうち、最新のものから最大10件までを取得するものとします。

### 部分ごとの詳細な説明:

1. `res = []`: 返すニュースフィードリストを初期化します。

2. `minHeap = []`: 最新のツイートを効率的に取得するためのミニマムヒープを初期化します。

3. `self.followMap[userId].add(userId)`: ユーザーが自身のツイートもニュースフィードに表示したいため、自分をフォローリストに追加します。

4. `for followeeId in self.followMap[userId]:`: ユーザーがフォローしている各ユーザーについてループ処理します。
   
    - `if followeeId in self.tweetMap:`: フォローしているユーザーがツイートを持っている場合のみ処理を進めます。
   
    - 以下の三行は、最新のツイートを取得し、ヒープに追加します。
   
5. `while minHeap and len(res) < 10:`: ヒープにツイートが存在し、`res`がまだ10件未満の場合、ループ処理を続けます。
   
    - 最も古いツイート（最小の`count`を持つもの）をヒープから取り出し、結果のリストに追加します。
   
    - そのフォローイのユーザーの次に新しいツイートがある場合、それをヒープに追加します。

6. `return res`: 最新の10件のツイートIDを含むリストを返します。

この実装では、ミニマムヒープを使用して最新のツイートを効率的に取得しています。ヒープを使用することで、常に最新のツイートを効率的に取得することができるため、ユーザーのニュースフィードに最新の情報を表示することができます。
"""

"""
この特定のコードのコンテキストにおいて、`hashset`（Pythonでの`set`）を使う理由は、フォロワーがフォローしているユーザー（フォローイ）の一意性を維持するためです。フォロワーは特定のフォローイを一度しかフォローできないため、`set`（集合）はその一意性を維持するのに最適です。`set`には以下の利点があります：

1. `set`内の要素は一意です。同じ要素を複数回追加しようとしても、実際には1つの要素として保存されます。
2. `set`では、要素の存在確認が平均的にO(1)の時間でできます。

対照的に、`hashmap`（Pythonでの`dict`）はキーと値のペアを保存します。この特定のケースでは、ユーザーのID（フォロワーやフォローイのID）だけを追跡しているため、追加の「値」が不要です。

もし`hashmap`を使用する場合、キーとしてユーザーIDを、値として何らかのダミー値（例：`True`や`1`など）を保存することになります。これは追加のメモリを消費し、コードの読みやすさも少し損なわれる可能性があります。

そのため、この特定のコードのコンテキストにおいて、フォロー関係を追跡するために`set`を使用することは、効率的かつ直感的です。
"""