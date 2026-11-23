class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1
        people.sort()
        l = res = 0
        r = len(people) - 1
        while l <= r:
            cur = limit - people[r]
            r -= 1
            if people[l] <= cur:
                l += 1
            res += 1
        return res