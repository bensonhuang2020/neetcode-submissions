class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = {}
        for ori, dest in sorted(tickets)[::-1]:
            if ori not in adj_list:
                adj_list[ori] = []
            adj_list[ori].append(dest)
        
        res = []
        def dfs(ori):
            while ori in adj_list and adj_list[ori]:
                dest = adj_list[ori].pop()
                dfs(dest)
            res.append(ori)
        
        dfs('JFK')
        return res[::-1]
