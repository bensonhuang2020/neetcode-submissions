class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # the naïve and initial idea that i have for solving this is that in the outer question, we traverse the matrix by going through all the grid coords in either directions that we can. we don't need to backtrack cause we only go for strictly increasing.
        memo = {}
        rows, cols = len(matrix), len(matrix[0])
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 1

            # check if we're on the borders and if the bordering is more than our current spot, if it is, then we can check it. no redundant work.

            if i + 1 < rows and matrix[i + 1][j] > matrix[i][j]:
                res = max(res, 1 + dfs(i + 1, j))

            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                res = max(res, 1 + dfs(i - 1, j))
            
            if j + 1 < cols and matrix[i][j + 1] > matrix[i][j]:
                res = max(res, 1 + dfs(i, j + 1))
            
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                res = max(res, 1 + dfs(i, j - 1))

            memo[(i, j)] = res


            return memo[(i, j)]



        for r in range(rows):
            for c in range(cols):
                dfs(r, c)
        
        return max(memo.values())

