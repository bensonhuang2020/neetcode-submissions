class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # what's the most naive way to approach this? we can't just remove the first one we see that would overlap with the next. i know for sure we want to start by sorting
        if len(intervals) == 1:
            return 0
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        # essentially, we always want to remove the one that ends later. hence, the "new end" to compare to is always the prior one that overlapped with. if start is >= prevEnd, this means that nothing changes since there is no overlap so go on.
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
