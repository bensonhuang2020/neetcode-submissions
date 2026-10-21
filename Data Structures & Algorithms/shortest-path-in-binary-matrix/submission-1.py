class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # i'm pretty sure we just do bfs with distance grid
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        # recreate a distance matrix
        distances = [[-1] * COLS for _ in range(ROWS)]
        distances[0][0] = 1
        dq = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        dq.append((0, 0))
        # run bfs in matrix, we only append if the location is a 0 and on distance grid, it is either -1 or worse than the prevdistance + 1 (new distance). hence the deque only gets increased if it has to. return the last grid when done, it should be min. it seems that takign the top left cell (the starting point) is considered a "move" and so is reaching the end. hence if either is already 1 on the grid, we can't reach it.
        while dq:
            r, c = dq.popleft()
            for x, y in directions:
                if x + r < 0 or x + r >= ROWS or y + c < 0 or y + c >= COLS:
                    continue
                if grid[x+r][y+c] == 0:
                    new_distance = distances[r][c] + 1
                    # we dont need or new_distance < distances[x+r][y+c] because the way bfs works is that the first time we modify it, it's the best anyways unless we had weights.
                    if distances[x+r][y+c] == -1:
                        distances[x+r][y+c] = new_distance
                        dq.append((x+r, y+c))
        return distances[ROWS-1][COLS-1]

    # time is O(M*N) representing every possible coordinate/grid location since it has to traverse all of them at worst
    # space is O(M*N) since we recreate the grid with distance.