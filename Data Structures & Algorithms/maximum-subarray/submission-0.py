class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # naively, i suppose we'd either choose to include the running sum or not for each solution. i'm honestly thinking of dp so we either choose to start anew or we continue the subarray.
        n = len(nums)
        memo = {}
        def find_max(i):
            if i in memo:
                return memo[i]

            # if we're at the end, we must always take
            if i == n - 1:
                return nums[i]

            # the logic here is either that we keep adding on and continuing or we stop here.
            memo[i] = max(nums[i] + find_max(i + 1), nums[i])

            return memo[i]

        # now we have to pretend that we start at each point, no skipping.
        return max(find_max(j) for j in range(len(nums)))