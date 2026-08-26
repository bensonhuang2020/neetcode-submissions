class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # using the normal binary search middle, we can assume that if we're in the middle, checking right side is smaller than middle means that the min is on the right side so we can move left to middle + 1 (can't be the middle itself)
            if nums[mid] > nums[r]:
                l = mid + 1
            # all inclusive would be nums[mid] <= nums[r] means that left side contains the sorted part. however, we now don't know if mid could be the correct number so we'd best keep it in the running and remove the right side
            else:
                r = mid
        # we can take nums[l] or nums[r] since at the exit they'd both be the same
        return nums[l]
