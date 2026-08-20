class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        key_list = list(sorted_dict.keys())
        for i in range(k):
            res.append(key_list[i])
        return res