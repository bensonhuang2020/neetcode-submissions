class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # intervals could be 0, in that case, we just return the new interval
        appended = False
        if not intervals:
            res.append(newInterval)
            return res

        for interval in intervals:
            if newInterval[1] < interval[0]:
                if not appended:
                    res.append(newInterval)
                    appended = True
                res.append(interval)

            
            elif interval[1] < newInterval[0]:
                res.append(interval)
            
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

        if not appended:
            res.append(newInterval)
        return res