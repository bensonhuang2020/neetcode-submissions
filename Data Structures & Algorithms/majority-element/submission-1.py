class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        seen = 1
        for i in range(1, len(nums)):
            if nums[i] == curr:
                seen += 1
            else:
                seen -= 1
                if seen == 0:
                    seen = 1
                    curr = nums[i]
        return curr 