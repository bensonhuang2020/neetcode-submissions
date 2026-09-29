class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # i think the way to approach this is that we start with the number of connected components as the number of components in general. each edge created means the number of connected components goes down by 1. however, if the edges are created between nodes that are in the same connected component, nothing happens to the total. how do we determine that? naive would be to fun cyclic detection, but it's costly.
        # easier way is just to do adjacency list creation, then run dfs from each node. if we find that the node is not in the visited, it's a new connected component. this one is more of a counting.

        # create adj list
        adj_list = {i: [] for i in range(n)}
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        # create visited set
        visited = set()
        count = 0
        # run dfs, if we already visited, then there's a cycle, no need to pursue
        def dfs(node):
            if node in visited:
                return False
            # else, we now visited and should visit the neighbors
            visited.add(node)
            for adj in adj_list[node]:
                dfs(adj)
            return True
        # since everything is in order, if we haven't visited, it's a new component.
        # run dfs again.
        for i in range(n):
            if i not in visited:
                count += 1
            dfs(i)
        return count
