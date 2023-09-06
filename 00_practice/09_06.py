from collections import defaultdict
from typing import List
import heapq

class Twitter:
    def __init__(self):

    def postTweet(self, userId: int, tweetId: int) -> None:

    def getNewsFeed(self, userId: int) -> List[int]:

    def follow(self, followerId: int, followeeId: int) -> None:

    def unfollow(self, followerId: int, followeeId: int) -> None:

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
print(obj.getNewsFeed(userId=1))
obj.unfollow(followerId=1,followeeId=2)
print(obj.getNewsFeed(userId=1))
print(obj.getNewsFeed(userId=2))
print(obj.getNewsFeed(userId=3))