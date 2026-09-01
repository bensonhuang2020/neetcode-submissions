class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a maxheap and pop twice then smash
        neg_stones = [-stone for stone in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) >= 2:
            first_stone = -heapq.heappop(neg_stones)
            second_stone = -heapq.heappop(neg_stones)
            if first_stone == second_stone:
                continue
            heapq.heappush(neg_stones, -(first_stone - second_stone))
        if not neg_stones:
            return 0
        return -neg_stones[0]