class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if we want to find the kth largest element, we'd convert the whole thing to a minheap, then since it's minimum, we'd find the difference from the length of the entire thing and k.
        nums_to_find = len(nums) - k
        heapq.heapify(nums)
        for i in range(nums_to_find):
            heapq.heappop(nums)
        # simply put, if we want the 3rd largest, we have 7 in a list and we make it a minheap, we don't get the 3rd largest item until we pop off item indexed at 4. this means since range(nums_to_find) does 0, 1, 2, 3, we're gonna have to pop one more for 5.
        return heapq.heappop(nums)