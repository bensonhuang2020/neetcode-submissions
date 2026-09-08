class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # find all of the treasure chests, put them in a queue, then run bfs to find distance to all of the land cells from each one. we'd have a mapping solution wise for each cell and it's min due to bfs
        queue = deque()

        # first traversal will populate the queue with treasures so that our bfs starts from the centers
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        # start bfs, we look in each direction. the first distances out from each treasure add 1 to 0, then we enter them into the queue. we keep the distances in the current cell itself. the way bfs works, we only increment outward using values on the queue, which either keep grabbing land radiating outwards or there's nothing so they don't change and don't get added to the queue.
        while queue:
            r, c = queue.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append((nr, nc))
