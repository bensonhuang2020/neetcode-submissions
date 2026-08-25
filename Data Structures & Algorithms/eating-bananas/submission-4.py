class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # slowest possible is 1 banana, fastest is all the bananas in 1 pile
        l, r = 1, max(piles)
        # k reps speed
        k = r
        while l <= r:
            # the binary search is based around the speed from left + right
            speed = (l + r) // 2

            # for each speed, we need to find if the allotted time is enough
            curr_time = 0
            for x in piles:
                # we have to ceil cause you find the number of hour koko can eat banana, and that counts as an extra hour
                curr_time += int(math.ceil(x / speed))
            
            #if the current time is less than allotted and she's eating faster, we have a new eating speed
            if curr_time <= h and speed < k:
                k = speed
            # if koko is eating faster than the alloted time, eating speed should decrease
            if curr_time <= h:
                r = speed - 1
            else:
                l = speed + 1
        return k