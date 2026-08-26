class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # inflection point is the minimum
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        # l is now the inflection point.
        # if the target is in the left side of the minimum, we must run bs on nums[0] and nums[l - 1]
        if l == 0:
            le, ri = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[(l-1) % len(nums)]:
            le, ri = 0, l - 1
        else:
            le, ri = l, len(nums) - 1
        
        while le <= ri:
            mid = (le + ri) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                le = mid + 1
            else:
                ri = mid - 1
        
        return -1

