class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
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
        print(dist)
        if last_time == float("inf"):
            return -1
        return last_time
