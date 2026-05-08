class Twitter:
    from collections import defaultdict
    def __init__(self):
        self.followMap = defaultdict(set) # userID -> followeIds
        self.count = 0 
        self.tweetMap = defaultdict(list) # userID -> (time, tweetID)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] 
        minHeap = []

        self.followMap[userId].add(userId)
        for user in self.followMap[userId]: # get most recent tweet for every user that userId follows
            if user in self.tweetMap:
                index = len(self.tweetMap[user]) - 1
                time, tweetId = self.tweetMap[user][index] 
                heapq.heappush(minHeap, [time, tweetId, user, index - 1])

        #heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, user, index = heapq.heappop(minHeap)
            res.append(tweetId) 
            if index > -1:
                time, tweetId = self.tweetMap[user][index]
                heapq.heappush(minHeap, [time, tweetId, user, index - 1]) 

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.followMap[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
        
