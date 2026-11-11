class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), 50000
        res = 0

        def ship(limit):
            day = 1
            w = 0
            for weight in weights:
                if w + weight > limit:
                    day += 1
                    w = 0
                w += weight
            return day <= days

        while l <= r:
            mid = (l + r) // 2
            if ship(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
