class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        total_water = 0

        # prefix represents the left wall, suffix represents the right wall
        # essentially, prefix[i] and suffix[i] represent the walls at the left and right side. so, for each position, since we need 2 walls, we'll create 2 arrays to hold the biggest left and right wall at each position.
        max_prefix = 0
        for i in range(len(height)):
            max_prefix = max(height[i], max_prefix)
            prefix[i] = max_prefix
        max_suffix = 0
        for j in range(len(height) - 1, -1, -1):
            max_suffix = max(height[j], max_suffix)
            suffix[j] = max_suffix
        
        # when we have the left and right walls for each position, we calculate how much water each position holds. the smaller wall indicates how much water can be held, hence the min. and then we use that and find the difference between current height since water is displaced directly from the current tile. the reason why we can't have negative is because the height of prefix and suffix at the current tile is either larger than the current tile or it is the current tile (hence either height calc or 0).
        for i in range(len(height)):
            total_water += min(prefix[i], suffix[i]) - height[i]

        return total_water