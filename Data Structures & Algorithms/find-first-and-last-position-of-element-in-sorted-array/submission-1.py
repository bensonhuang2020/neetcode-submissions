class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # run binary search to find the target existing, then we can expand both directions until we either run out or we can binary search the last location for the target
        if not nums:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        idx = [-1, -1]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                break
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[mid] != target:
            return idx
        # let's go left first:
        for i in range(mid, -1, -1):
            if nums[i] != target:
                i += 1
                break
        for j in range(mid, len(nums)):
            if nums[j] != target:
                j -= 1
                break
        idx = [i, j]
        return idx
