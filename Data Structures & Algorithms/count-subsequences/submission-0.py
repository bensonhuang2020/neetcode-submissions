class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # keep 2 indices, decide to iterate for either one
        memo = {}
        m, n = len(s), len(t)

        def distinct(i, j):
            # if our s index is oob and our t index isn't, means that we didn't match through.
            if i >= m and j < n:
                return 0

            # if j >= n, it means that we matched fully through
            if j >= n:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]
            
            # we can always choose not to take the current s char
            memo[i, j] = distinct(i + 1, j)
            # can only take the current s char if it matches the t char.
            if s[i] == t[j]:
                memo[(i,j)] += distinct(i + 1, j + 1)
            
            return memo[(i, j)]
        
        # because we do the iteration on every char of take or no take, we don't need a for loop outside.
        return distinct(0, 0)
            