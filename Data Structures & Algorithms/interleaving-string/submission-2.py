class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # i think we should probably show that the decision tree is that we can either advance the index for s1 (i) or the index for s2 (j). at the end, i + j should equate to length of s3
        m, n, o = len(s1), len(s2), len(s3)
        # specific case where if len of s3 is less than s1 and s2 combined, it's not possible to interleave to reach that solution.

        if o != m + n:
            return False
        memo = {}
        def interleave(i, j):
            if i + j == o:
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            can_change = False
            
            if i < m and s1[i] == s3[i + j]:
                can_change = can_change or interleave(i + 1, j)
            
            if j < n and s2[j] == s3[i + j]:
                can_change = can_change or interleave(i, j + 1)
            
            memo[(i, j)] = can_change
            
            return memo[(i, j)]

        return interleave(0, 0)