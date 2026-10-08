class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
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
