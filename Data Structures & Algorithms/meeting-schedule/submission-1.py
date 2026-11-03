"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # since we sorted the entire array by the start time, it means that each subsequent start time is the one right after the end time. if there's a conflict, we greedily take the next one so it's not like any other one would be in the ending time. hence, if they're both in the same time, they'd show conflict anyways.
        if len(intervals) <= 1:
            return True
        intervals.sort(key=lambda i: i.start)
        cur_interval = intervals[0]
        for i in range(1, len(intervals)):
            if cur_interval.end > intervals[i].start:
                return False
            cur_interval = intervals[i]
        return True

