class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # important things to note, choosing a different direction doesn't necessarily mean a new path. it should be considered a new path when we reach the bottom right.
        # naive solution is to choose a direction to increment until we hit i == (m - 1) or j == (n - 1), we should implement some memoization to it
        memo = {}
        def traverse(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i > m or j > n:
                return 0
            if i == (m - 1) or j == (n - 1):
                return 1
                
            memo[(i, j)] = traverse(i + 1, j) + traverse(i, j + 1)

            return memo[(i, j)]
        return traverse(0, 0)

