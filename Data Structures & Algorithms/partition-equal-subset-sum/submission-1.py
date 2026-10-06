class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # the biggest insight is that if the total sum isn't even, then we can't even solve.
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        # target is to find half of the sum in 1 partition, the other partition handles it
        n = len(nums)
        # fun thing is that hash sets can take tuples as keys
        memo = {}
        
        # for each step in the recursion, we iterate through the list of nums and we want the target to equate to 0.
        def part(index, curr_target):
            # if the index is greater than the lenght, we failed
            if index >= n:
                return False
                # if the target is not 0, we failed
            if curr_target <= 0:
                return curr_target == 0
                # not redundant work
            if (index, curr_target) in memo:
                return memo[(index, curr_target)]
            
            # we either don't take the current index and move on or we take and we move on. in both cases, we increment the index, the main difference is whether we subtract from the curr_target.
            memo[(index, curr_target)] = part(index + 1, curr_target) or part(index + 1, curr_target - nums[index])

            return memo[(index, curr_target)]

        return part(0, target)
            
                