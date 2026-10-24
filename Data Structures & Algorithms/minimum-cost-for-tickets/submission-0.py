class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        length = len(days)
        durations = [1, 7, 30]
        def travel(i):
            if i >= length:
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = float("inf")
            for k in range(3):
                j = i
                while j < len(days) and days[j] < days[i] + durations[k]:
                    j += 1
                dp[i] = min(dp[i], costs[k] + travel(j))
            
            return dp[i]
        return travel(0)
            