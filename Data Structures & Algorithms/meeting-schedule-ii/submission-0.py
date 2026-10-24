"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort all of the rooms start first
        if len(intervals) <= 1:
            return len(intervals)

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        # essentially, we want all of the starts and finishes. we don't care which end is for which start. we only care that each start before an end is another room we need to book. we only care for the max count of the room
        res = count = 0
        s = e = 0
        while s < len(intervals):
            # starts at 0 for both, will increment to see if the end is before the start of the next interval
            # very simple concept. we have the ends and the starts. the number of running meetings is the difference between the 
            if start[s] < end[e]:
                s += 1
                count += 1
                res = max(count, res)
            else:
                e += 1
                count -= 1

        return res
        