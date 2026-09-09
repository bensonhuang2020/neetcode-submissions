class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # essentially, we wanna run dfs to add to sets for each tile that can be reached from pacific and atlantic oceans. if we ever hit a point where the current tile is shorter than the previous tile, this means that it can't be reached
        row, col = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevHeight):
            # this part is a bit confusing, but we're running dfs from the ocean, meaning that the water can only come to us if it's lower cause if it were higher, it wouldn't be able to come from the ocean itself.
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == row or c == col or
                heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # this represents the top and bottom borders

        for c in range(col):
            dfs(0, c, pacific, heights[0][c])
            dfs(row - 1, c, atlantic, heights[row - 1][c])

        # this represents the left and right borders.
        for r in range(row):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, col - 1, atlantic, heights[r][col - 1])

        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r, c])
        return res