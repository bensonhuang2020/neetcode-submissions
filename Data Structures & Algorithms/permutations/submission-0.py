class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def perm(curr, new_nums):
            nonlocal res
            for i in range(len(new_nums)):
                curr.append(new_nums[i])
                if len(curr) == len(nums):
                    res.append(curr[:])
                else:
                    perm(curr, new_nums[:i] + new_nums[i+1:])
                curr.pop()
        perm([], nums)
        return res