"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        # sort then check overlaps
        intervals.sort(key=lambda i: i.start)
        cur_interval = intervals[0]
        for i in range(1, len(intervals)):
            if cur_interval.end > intervals[i].start:
                return False
            cur_interval = intervals[i]
        return True