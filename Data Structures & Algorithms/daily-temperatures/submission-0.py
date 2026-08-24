class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for x in range(len(temperatures)):
            while stack and temperatures[x] > stack[-1][0]:
                res = stack.pop()
                result[res[1]] = x - res[1]
            stack.append((temperatures[x], x))
        return result