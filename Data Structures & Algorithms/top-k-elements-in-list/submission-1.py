class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        # sorted_list = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        # key_list = list(sorted_dict.keys())
        # for i in range(k):
        #     res.append(key_list[i])
        # return res
        heap_list = [(-item[1], item[0]) for item in freq.items()]
        heapq.heapify(heap_list)
        for i in range(k):
            res.append(heapq.heappop(heap_list)[1])
        return res
