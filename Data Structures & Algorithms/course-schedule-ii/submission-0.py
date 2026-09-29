class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # we need to create the graph and find a cycle again, but with the dfs, we should also keep track of the possible path when traversing. to keep the traversal time fast, we should try to create the course path while determining cycle.
        prereqs = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        # much like the previous question, we want to set up the adjacency list to start with the dict having key = curr course, list contains pre-reqs
        res = []
        visited, cycle = set(), set()
        # we want 2 lists, 1 to contain the current cycle tracking much like the previous question, with the other list to indicate if we've already seen this 
        def traverse(crs):
            # this follows suit, where if we already have in cycle, we don't have to continue and it propagates as False. if in visited, we return True since we've already explored it and handled all the pre-reqs.
            if crs in cycle:
                return False
            if crs in visited:
                return True

            # we add to cycle first since we know that something has to be in cycle when we look at it at first -- if it shows again later, it means that we have a cycle
            cycle.add(crs)
            for pre in prereqs[crs]:
                # run through all the pre-reqs first
                if traverse(pre) == False:
                    return False
            # remove the current course after the children finish processing
            cycle.remove(crs)
            # once we've finished processing all of the children, we can add the current one into the visited path and the result
            visited.add(crs)
            res.append(crs)
            return True
            
        for c in range(numCourses):
            # it's not necessary that all of them are connected, so we'll hvae to run the DFS on each course
            if traverse(c) == False:
                return []
        return res
            
