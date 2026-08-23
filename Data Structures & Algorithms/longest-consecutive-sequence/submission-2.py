class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_run = 0
        current_run = 0
        for i in set_nums:
            if i - 1 not in set_nums: # this is the start of a consecutive sequence
                j = i + 1
                current_run = 1
                while j in set_nums: # keep finding until the end
                    j += 1
                    current_run += 1
            if current_run > max_run: # take the max
                max_run = current_run
        return max_run