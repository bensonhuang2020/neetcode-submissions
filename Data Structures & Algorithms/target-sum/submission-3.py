class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # thought process is that we can take a decision to add or subtract the number from each point. dp is just finding number of decisions that can be made.if it's in memo, we already found, no need for duplicate work. we must go through the whole list as is, just need to make sure that the rolling sum/value is equal to target. the memo value is the number of ways if subtracting or adding the current value, start at the first index and amount as 0.
        n = len(nums)
        memo = {}
        
        def find_target(index, amount):
            if (index, amount) in memo:
                return memo[(index, amount)]

            if index == n:
                if amount == target:
                    return 1
                return 0
            
            memo[(index, amount)] = find_target(index + 1, amount - nums[index]) + find_target(index + 1, amount + nums[index])

            return memo[(index, amount)]
        
        return find_target(0, 0)
