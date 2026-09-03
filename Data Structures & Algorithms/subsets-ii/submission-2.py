class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        res.append([])

        # same thing as the first time we saw it, but now we have to sort it so that if we have a duplicate in the same depth (same functional call), we don't want to rebranch
        def subs(curr, index):
            nonlocal res
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                res.append(curr[:])
                subs(curr, i + 1)
                curr.pop()

        subs([], 0)
        return res