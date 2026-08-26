class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # from the example, it looks like if the left is less than the mid, the sorted must be on the right side
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
