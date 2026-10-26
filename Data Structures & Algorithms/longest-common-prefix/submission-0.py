class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find the shortest length
        n = len(strs) - 1
        pref_length = len(min(strs, key=len))

        res = ""
        while pref_length != 0:
            comp = strs[0][:pref_length]
            for i in range(len(strs)):
                if not strs[i].startswith(comp):
                    pref_length -= 1
                    break
            if i == n and strs[i].startswith(comp):
                return comp

        return res
