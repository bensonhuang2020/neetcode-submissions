class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_vol = 0

        # we greedily want the best heights. if one height is worse, we go to the other. we greedily also take heights, and if they're shorter, we won't get better. biggest width is always going to come earlier.
        while l < r:
            max_vol = max(max_vol, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return max_vol