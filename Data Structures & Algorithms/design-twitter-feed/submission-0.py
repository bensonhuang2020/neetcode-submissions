class Twitter:

    def __init__(self):
        self.count = 0
        # follow list is a set since we can't follow the same person more than once and would cause dupes. tweet map is a list since we only post a tweet 1x anyways.
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        # each count is decreasing so that when we run through a minHeap, more recent ones show up first

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # user sees their own posts
        self.followMap[userId].add(userId)
        
        # for each user following, we push out the tweet into the heap
        for user_id in self.followMap[userId]:
            for tweet in self.tweetMap[user_id]:
                heapq.heappush(minHeap, tweet)
        # we either look through the 10 most recent tweets or we're out of tweets to look out
        for i in range(10):
            if not minHeap:
                break
            res.append(heapq.heappop(minHeap)[1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # set, so we add a followee for a certain user to follow
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if we unfollow, jsut remove from set
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
