class Twitter:
    import heapq
    from collections import defaultdict
    def __init__(self):
        self.followMap = defaultdict(set) # userId -> hash set of followee's
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetId]
        self.count = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        tweets = []
        maxHeap = [] 

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap: 
                index = len(self.tweetMap[followeeId]) - 1 
                count, tweetId = self.tweetMap[followeeId][index]
                maxHeap.append([-count, tweetId, followeeId, index - 1])

        heapq.heapify(maxHeap)
        while maxHeap and len(tweets) < 10: 
            count, tweetId, followeeId, index = heapq.heappop(maxHeap) 
            tweets.append(tweetId) 
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])
        
        return tweets


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

