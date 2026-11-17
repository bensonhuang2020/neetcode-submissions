class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # essentially, this is just bfs, but for every side that's not connected to land from all four sides, we just add to the perimeter. going to assume that there's only 1 island.
        perimeter = 0
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # let's make sure that we add the coords to the visited set as we add to the queue so we don't add them back in the queue twice and doublecount.
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q = deque()
                    visited = set()
                    q.append((i, j))
                    visited.add((i, j))
                    while q:
                        x, y = q.pop()
                        for a, b in directions:
                            if (a+x, b+y) in visited:
                                continue
                            if (a+x) < 0 or (a+x) == n:
                                perimeter += 1
                            elif (b+y) < 0 or (b+y) == m:
                                perimeter += 1
                            elif grid[a+x][b+y] == 0:
                                perimeter += 1
                            else:
                                q.append((a+x, b+y))
                                visited.add((a+x,b+y))
                    return perimeter
                        
