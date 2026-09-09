class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # add the rotten fruit into a queue. pop left until queue is empty, keep a running time counter + count 
        q = deque()
        total = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    total += 1
        
        time = 0
        counting = 0
        while q and counting < total:
            # key insight for capturing the time movement is to make sure that we process in batches.
            time_size = len(q)
            for i in range(time_size):
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        counting += 1
            time += 1


        if counting == total:
            return time
        return -1