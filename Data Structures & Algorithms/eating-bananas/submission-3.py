class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            speed = (l + r) // 2
            curr_time = 0
            for x in piles:
                curr_time += int(math.ceil(x / speed))
            if curr_time <= h and speed < k:
                k = speed
            if curr_time <= h:
                r = speed - 1
            else:
                l = speed + 1
        return k