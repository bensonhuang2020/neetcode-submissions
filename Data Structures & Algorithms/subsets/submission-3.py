class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        if not nums:
            return res

        def build_subset(curr, index):
            nonlocal res
            """
            # for each index, we create a new list based on our current list. starts with [], so it's just empty lists. we're using curr as the base case, then we add a list number, which appends to the current list. result takes this as a result, then recursively call the list with this as a starting point. this does the backtracking.
            for i in range(index, len(nums)):
                new_list = curr[:] + [nums[i]]
                res.append(new_list)
                build_subset(new_list, i + 1)
            """
            # backtracking style, append the current item, then append the current list to the result, explore with recursive call, then pop the most recent item to effectively "backtrack".
            for i in range(index, len(nums)):
                curr.append(nums[i])
                res.append(curr[:])
                build_subset(curr, i + 1)
                curr.pop()
        build_subset([], 0)
        return res