class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        def backtrack(i, subset):
            nonlocal res
            xorr = 0
            for num in subset:
                xorr ^= num
            res += xorr

            for j in range(i, n):
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()
            
        backtrack(0, [])
        return res