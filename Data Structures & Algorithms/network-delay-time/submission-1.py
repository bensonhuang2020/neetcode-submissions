class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # simply put, we create an adjacency list and keep a list of distances. the adjacency list represents the directed graph unidirectionally with tuples in a list. since it's 1 indexed, i'm incentivized to create an n + 1 size array for the distance. then, we need to set distance to 0 for the starting point and put it in a queue. set the 0th also to 0 since we're never reaching it and it's going to mess up calculations.
        adj_list = {}
        dist = [float("inf")] * (n + 1)
        for origin, target, time in times:
            if origin not in adj_list:
                adj_list[origin] = []
            adj_list[origin].append((target, time))
        dist[k] = 0
        dist[0] = -1
        q = deque()
        q.append(k)

        # run the bfs function where we only update distance if it's less than infinity or the current dist. then, we check the max distance since that's what we want (the longest time).
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node not in adj_list:
                    continue
                for target, time in adj_list[node]:
                    if time + dist[node] < dist[target]:
                        dist[target] = time + dist[node]
                        q.append(target)

        last_time = max(dist)

        if last_time == float("inf"):
            return -1
        return last_time
