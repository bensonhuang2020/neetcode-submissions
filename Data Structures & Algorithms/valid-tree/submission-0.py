class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # there can be no cycles and the nodes must be fully connected
        # how do we find that there are no cycles? 
        # start with an adjacency list, ensure that each node is connected with the others

        # create the adjacency list
        adj_list = {i : [] for i in range(n)}
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        visited = set()

        # we need parent so that we know that when we make the adjacency list, the neighbor being the parent doesn't cause a cycle
        def dfs(node, parent):
            # already being in visited means cycle
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj_list[node]:
                if parent == neighbor:
                    continue
                    # if we get false from dfs call from iteration, it's a cycle.
                if not dfs(neighbor, node):
                    return False
            return True
        # we start off with parent being non-existent, shouldn't be the reason why we fail but it's the first labeled node
        if not dfs(0, -1):
            return False
        # at the very end, we must check if all the nodes are connected from adjacency list from the first first one. the len of the visited shows that the dfs can hit all the nodes.
        return len(visited) == n
        
        