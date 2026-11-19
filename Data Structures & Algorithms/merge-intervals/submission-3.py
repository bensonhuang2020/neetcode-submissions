class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # this is the same as the other intervals question except that it's not already sorted and newInterval is the current interval. our "newInterval" that we're looking at is the first one. so we don't have to consider the very first in the for loop. if the current intervals end is smaller than the new iterative one, then we just append the current and make the iterative the new current. otherwise, we want to keep overlapping intervals. the min or the start interval is alwasy going to be the current interval's because the array is already sorted, so the number we're already looking at will always be the smaller of the two. for the max of the overlap, we can just use the max of the current interval and the next number. continue with either building out the current interval or adding the next value. we have to add in the last current interval since we've gone through for loop and have no mechanism to determine to add the last loop. 
        intervals.sort()

        res = []
        if len(intervals) == 1:
            return intervals
        
        curInterval = intervals[0]

        for i in range(1, len(intervals)):
            if curInterval[1] < intervals[i][0]:
                res.append(curInterval)
                curInterval = intervals[i]
            else:
                curInterval = [curInterval[0], max(intervals[i][1], curInterval[1])]
        
        res.append(curInterval)

        return res
