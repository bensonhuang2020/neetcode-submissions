class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # using a maxHeap created from the euclidean coords, we can just keep at most k entries, probably just remove off the top
        heap = []
        for point in points:
            distance = (point[0] * point[0]) + (point[1] * point[1])
            heapq.heappush(heap, (-distance, (point[0], point[1])))
            if len(heap) > k:
                heapq.heappop(heap)
        return [coordinate[1] for coordinate in heap]