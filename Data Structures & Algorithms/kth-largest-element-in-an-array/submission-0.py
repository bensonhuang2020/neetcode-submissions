class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if we want to find the kth largest element, we'd convert the whole thing to a minheap, then since it's minimum, we'd find the difference from the length of the entire thing and k.
        nums_to_find = len(nums) - k
        heapq.heapify(nums)
        for i in range(nums_to_find):
            heapq.heappop(nums)
        return heapq.heappop(nums)