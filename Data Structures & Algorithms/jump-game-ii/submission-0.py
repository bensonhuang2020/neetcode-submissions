class Solution:
    def jump(self, nums: List[int]) -> int:
        # the most expensive way would be to start from the front and try every reachable step.
        """
        goal = len(nums) - 1
        def minJumps(position):
            if position >= goal:
                return 0
            if nums[position] == 0:
                return len(nums)
            min_answer = len(nums)
            for i in range(1, nums[position] + 1):
                min_answer = min(1 + minJumps(position + i))
            return min_answer
        return minJumps(0)
        """
        res = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            # we want the window to be the maximum range you can jump between on the current set of tiles, inclusive of r since that's both the landing spot and a jumpable location. the furthest goes from every location jumpable and we just make the furthest the max. we want every travelable location so we just do l = r + 1 because we know that since there's always an answer, we will 100% hit every spot.
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l = r + 1
            r = furthest
            res += 1
        return res
