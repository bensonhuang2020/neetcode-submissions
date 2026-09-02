class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        if not nums:
            return res

        def build_subset(curr, index):
            nonlocal res
            for i in range(index, len(nums)):
                new_list = curr[:] + [nums[i]]
                res.append(new_list)
                build_subset(new_list, i + 1)

        build_subset([], 0)
        return res