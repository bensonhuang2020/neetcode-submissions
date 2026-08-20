class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashes = defaultdict(list)
        #let's just make a list of sorted words
        for i in range(len(strs)):
            hashes[tuple(sorted(strs[i]))].append(i)
        
        for bucket in hashes.keys():
            res = []
            for x in hashes[bucket]:
                res.append(strs[x])
            result.append(res)
        return result