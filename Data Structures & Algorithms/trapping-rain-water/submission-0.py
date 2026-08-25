class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        total_water = 0

        max_prefix = 0
        for i in range(len(height)):
            max_prefix = max(height[i], max_prefix)
            prefix[i] = max_prefix
        max_suffix = 0
        for j in range(len(height) - 1, -1, -1):
            max_suffix = max(height[j], max_suffix)
            suffix[j] = max_suffix
        
        for i in range(len(height)):
            total_water += min(prefix[i], suffix[i]) - height[i]
            
        return total_water