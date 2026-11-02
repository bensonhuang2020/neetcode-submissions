class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # we should take a greedy approach
        # if we sort with reverse = False (normal), we can keep track of the number of boats, left and right. we choose the last boat, we go until left and right are the same boat. if we choose the last boat, we choose the first and see if both ppl can fit. if not, we only move the right person since they wouldn't fit anyone else anyways.
        people.sort()
        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            if people[l] <= remain:
                l += 1
            res += 1
        return res

# O(nlogn) for time, O(1) for space
