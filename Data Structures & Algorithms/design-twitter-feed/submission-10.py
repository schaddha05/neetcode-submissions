class Twitter:
    from collections import defaultdict
    def __init__(self):
        self.followMap = defaultdict(set) # userID -> followeIds
        self.count = 0 
        self.tweetMap = defaultdict(list) # userID -> (time, tweetID)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        time = self.count 
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append([time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for tweet in self.tweetMap[userId]:
            tweets.append(tweet) 
        for user in self.followMap[userId]:
            for tweet in self.tweetMap[user]: 
                tweets.append(tweet) 
        tweets.sort(reverse = True)
        
        res = []
        j = 0
        for i in range(len(tweets)):
            res.append(tweets[i][1])
            j += 1
            if j == 10:
                return res
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.followMap:
            self.followMap[followerId] = set() 
        self.followMap[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
        
