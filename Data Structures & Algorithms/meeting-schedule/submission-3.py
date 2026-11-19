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
        intervals.sort(key=lambda i: i.start)
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if cur.end <= intervals[i].start:
                cur = intervals[i]
            else:
                return False
        return True