class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # if the newInterval is less than the right side, then we just append and we have the rest
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if the newInterval is greater than the greater of hte current interval, we just append the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # otherwise, the current interval is within range and should expand the newInterval so we should just keep eating it in.
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        # if we finish the whole loop and there's no new interval added, we added it at the end.
        res.append(newInterval)
        return res