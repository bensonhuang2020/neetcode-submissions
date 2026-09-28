class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # just have to set up a graph and find a cycle.
        # if there is no cycle, we are fine.

        # first question is how to build the graph, then how do we recognize the cycle?
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if graph[crs] == []:
                # there is no prereq
                return True
            visit.add(crs)
            for pre in graph[crs]:
                # if a cycle is ever found in the visited, we're done
                if not dfs(pre):
                    return False

            visit.remove(crs)
            # remove off of visited if not since we don't want to revisit the old.
            # if the node should have already been in a cycle, then we would've found it
            graph[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
