class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # the bad solution, naive way that would be very inefficient, (exponential x^2) would be going through the entire list and for each element, attempt to find take as we go along. just include and don't include for each one, we'd find the max length of the recursive, but it's too long.
        n = len(nums)
        memo = [-1] * n

        # set up the memoization to have each index minimized. in the inner function, if we've ever changed the memoized index, we should just return to avoid doing redundant work. lis for each index should initialize at 1 since the smallest lis is AT LEAST 1. for each index from then on, we should just check if the next index interated through is greater than the current index. if it is, we can choose to include it, then we should find the max. in the outer fucntion, we run a for loop to simulate taking each of the elements as the first in the lis. we just need the max of the memo now since that represents the greatest lis.


        def recurse(index):
            if memo[index] != -1:
                return memo[index]

            lis = 1

            for j in range(index + 1, n):
                if nums[j] > nums[index]:
                    lis = max(lis, 1 + recurse(j))
            
            memo[index] = lis

            return lis
        
        for i in range(len(nums)):
            recurse(i)
        return max(memo)