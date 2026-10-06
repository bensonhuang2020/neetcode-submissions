class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        n = len(nums)
        memo = {}
        
        # for each step in the recursion, we iterate through the list of nums and we want the target to equate to 0.
        def part(index, curr_target):
            if index >= n:
                return False
            if curr_target <= 0:
                return curr_target == 0
            if (index, curr_target) in memo:
                return memo[(index, curr_target)]
            
            memo[(index, curr_target)] = part(index + 1, curr_target) or part(index + 1, curr_target - nums[index])

            return memo[(index, curr_target)]

        return part(0, target)
            
                