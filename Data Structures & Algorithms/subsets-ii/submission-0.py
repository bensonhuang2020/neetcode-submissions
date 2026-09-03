class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        res.append([])

        def subs(curr, index):
            nonlocal res
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1] or nums[i] in res:
                    continue
                curr.append(nums[i])
                res.append(curr[:])
                subs(curr, i + 1)
                curr.pop()

        subs([], 0)
        return res