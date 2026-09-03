class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if not nums:
            return []

        def sums(curr, index, total):
            nonlocal res
            # keep track of total so that we just add 2 numbers, not the entire list at once every time so we do O(1) vs O(n)
            for i in range(index, len(nums)):
                curr.append(nums[i])
                new_total = total + nums[i]
                if new_total == target:
                    res.append(curr[:])
                elif sum(curr) < target:
                    # if we're less, we add the current number still since that could be a solution, however, we still want to pop off the newest item to backtrack
                    sums(curr, i, new_total)

                curr.pop()
        
        sums([], 0, 0)
        return list(res)
                