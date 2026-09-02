class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if not nums:
            return []

        def sums(curr, index, total):
            nonlocal res
            for i in range(index, len(nums)):
                curr.append(nums[i])
                new_total = total + nums[i]
                if new_total == target:
                    res.append(curr[:])
                elif sum(curr) < target:
                    sums(curr, i, new_total)

                curr.pop()
        
        sums([], 0, 0)
        return list(res)
                