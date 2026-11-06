class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # the naïve and initial idea that i have for solving this is that in the outer question, we traverse the matrix by going through all the grid coords in either directions that we can. we don't need to backtrack cause we only go for strictly increasing.
        memo = {}
        # don't need a visited since it's strictly increasing
        rows, cols = len(matrix), len(matrix[0])

        # check all 4 directions and that's your result + 1. we can use dp cause each tile only has 1 max dp.
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            
            res = 1
            if i + 1 < rows and matrix[i][j] < matrix[i + 1][j]:
                res = max(res, 1 + dfs(i + 1, j))
            
            if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
                res = max(res, 1 + dfs(i - 1, j))
            
            if j + 1 < cols and matrix[i][j] < matrix[i][j + 1]:
                res = max(res, 1 + dfs(i, j + 1))
            
            if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
                res = max(res, 1 + dfs(i, j - 1))
            
            memo[(i, j)] = res
            return res
        
        # run through every possible starting point
        longest = 0
        for x in range(rows):
            for y in range(cols):
                longest = max(dfs(x, y), longest)
        
        return longest
        