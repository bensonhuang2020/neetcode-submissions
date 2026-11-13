class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        times = [[float("inf") for _ in range(n)] for _ in range(n)]
        times[0][0] = grid[0][0]
        dq = deque()
        dq.append((0,0))
        possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while dq:
            for i in range(len(dq)):
                x, y = dq.popleft()
                for a, b in possible_moves:
                    if x + a >= 0 and x + a < n and y + b >= 0 and y + b < n:
                        new_time = max(times[x][y], grid[a+x][b+y])
                        if new_time < times[a+x][b+y]:
                            times[a+x][b+y] = new_time
                            dq.append((a+x, b+y))
        
        return times[n-1][n-1]
    
        