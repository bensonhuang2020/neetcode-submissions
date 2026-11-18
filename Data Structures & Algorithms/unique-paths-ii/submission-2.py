class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 1
        dp = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        def traverse(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                dp[(i, j)] = 0
                return dp[(i, j)]
            
            elif (i == m-1) and (j == n-1):
                return 1
            
            else:
                dp[(i, j)] = traverse(i + 1, j) + traverse(i, j + 1)
            
            return dp[(i, j)]
        
        return traverse(0, 0)
            