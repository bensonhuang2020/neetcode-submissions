class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # the brute force simple solution is that you just traverse the array until and keep track of the max as you go
        """
        max_prod = 0
        for i in range(len(nums)):
            curr_val = nums[i]
            max_prod = max(max_prod, curr_val)
            for j in range(i + 1, len(nums)):
                curr_val *= nums[j]
                max_prod = max(max_prod, curr_val)
        return max_prod
        """
        # another interesting approach does it differently by doing a sliding window where 0 makes the whole thing 0, negative numbers, if in odd values, makes the thing fail. positive only. so we must either cut from the left or keep going right.

        # so your result is the first number to start
        res = nums[0]
        # curMin and curMax is the rolling max or min
        curMin, curMax = 1, 1
        for num in nums:
            # going down the line, we have to keep tmp with the curMax and num multiplied values since we're going to mod curMax
            tmp = curMax * num
            # curMax either resets with the current number or, you take the running min and get the negative multiplied with it
            curMax = max(tmp, curMin * num, num)
            # the min takes the opposite, but yeah we want to keep the min in case a huge negative lets us make a huge positive.
            curMin = min(tmp, curMin * num, num)
            res = max(curMax, res)
        return res
