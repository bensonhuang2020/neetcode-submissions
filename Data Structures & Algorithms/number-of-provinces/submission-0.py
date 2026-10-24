class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # i think we just find the number of connected components in the graph
        # simply put, we have a visited array, if we haven't seen it yet, we add it to the dfs and the visited = True
        n = len(isConnected)
        res = 0
        visited = [False] * n

        # essentially, if the node in the grid is == 1, that means we're connected and it goes in visited
        # the for loop on the bottom does the dfs through neighbors, but each time we find something not in the visited, it's not a part of the connections and is new.
        def dfs(node):
            visited[node] = True
            for neighbor in range(n):
                if isConnected[node][neighbor] and not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1
        return res