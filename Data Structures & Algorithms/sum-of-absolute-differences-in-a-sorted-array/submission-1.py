class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # brute force is simple, but it's going to be O(n^2), which is pretty gross.

        # non bruteforce is finding prefix and suffix sums. using the prefix sums, we can find the sum of all the digits smaller than the one we're looking at, and hte suffix sums lets us find the digits that are greater. provided we find both, we just have to multiply by the number of values that are smaller and subtract the prefix from that, and do the opposite for the suffix.
        n = len(nums)
        prefixes = [0] * (n + 1)
        suffixes = [0] * (n + 1)
        res = []
        prefix = suffix = 0
        for i in range(n):
            prefixes[i] = prefix
            prefix += nums[i]
        for j in range(n-1, -1, -1):
            suffixes[j] += suffix
            suffix += nums[j]
        
        for l in range(n):
            curr = l * nums[l] - prefixes[l]
            curr += suffixes[l] - (n - l - 1) * nums[l]
            res.append(curr)
        return res

            
