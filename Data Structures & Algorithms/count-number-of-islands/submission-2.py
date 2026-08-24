class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # keep a set of visited coords
        visited = set()

        # running count of islands
        number_of_islands = 0

        stack = []

        # do tile by tile
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        number_of_islands += 1
                        visited.add((i, j))
                        stack.append((i, j))
                    
                    while stack:
                        x, y = stack.pop()
                        if x > 0 and grid[x-1][y] == "1" and (x-1, y) not in visited:
                            visited.add((x-1, y))
                            stack.append((x-1, y))
                        # if we're not on bottom edge and below us is in visited (meaning it's land, we're not a new island)
                        if x < len(grid) - 1 and grid[x+1][y] == "1" and (x+1, y) not in visited:
                            visited.add((x+1, y))
                            stack.append((x+1, y))
                        # so on so forth
                        if y > 0 and grid[x][y-1] == "1" and (x, y-1) not in visited:
                            visited.add((x, y-1))
                            stack.append((x, y-1))
                        if y < len(grid[0]) - 1 and grid[x][y+1] == "1" and (x, y+1) not in visited:
                            visited.add((x, y+1))
                            stack.append((x, y+1))

        return number_of_islands