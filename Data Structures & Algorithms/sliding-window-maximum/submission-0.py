class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        res.append(-max_heap[0][0])

        for j in range(k, len(nums)):

            # Add new element
            heapq.heappush(max_heap, (-nums[j], j))

            # while the max element is not in the range specified, we want to pop it off since it's stale until we find out that is.
            while max_heap[0][1] <= j - k:
                heapq.heappop(max_heap)
            res.append(-max_heap[0][0])
        return res
