from collections import defaultdict
import heapq

class Twitter(object):

    def __init__(self):
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0  # Decreasing time for latest tweets

    def postTweet(self, userId, tweetId):
        self.time -= 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        self.followees[userId].add(userId)

        tweets = []
        for followee in self.followees[userId]:
            tweets.extend(self.tweets[followee])

        # Get 10 most recent tweets
        top_10 = heapq.nsmallest(10, tweets)

        return [tweetId for time, tweetId in sorted(top_10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)
        self.followees[followerId].add(followerId)

    def unfollow(self, followerId, followeeId):
        if followeeId != followerId:
            self.followees[followerId].discard(followeeId)
