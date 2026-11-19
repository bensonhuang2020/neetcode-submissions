"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
    
        s, e, n = 0, 0, len(intervals)
        res, count = 0, 0
        while s < n:
            if starts[s] < ends[e]:
                count += 1
                s += 1
                res = max(count, res)
            else:
                e += 1
                count -= 1
        
        return res
        
            