class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # make a minheap that only holds k values. by the way a heap works, the smallest value will then be the kth largest. we only care about the kth largest anyways.
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # remove until we have k items, the top item we peek at is kth largest.
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
