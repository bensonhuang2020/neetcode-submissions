class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        # let's make sure that the starting points are all in order first
        intervals.sort()
        # the naive way to handle things would be to consider each interval as the "newInterval" from the last question where we use it as the pivot against the rest of the list going forward, but this is n^2 runtime since we loop through so often.
        res = []
        new_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= new_interval[1]:
                new_interval = [min(intervals[i][0], new_interval[0]), max(intervals[i][1], new_interval[1])]
            else:
                res.append(new_interval)
                new_interval = intervals[i]

        if new_interval:
            res.append(new_interval)
        return res
        
            
