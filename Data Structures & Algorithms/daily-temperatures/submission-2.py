class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # concept is that you iterate through the list. for each time you find a hotter day than what's on the stack, you find the difference in days. repeat until the hotter day is no longer hotter
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            # the way the stack works, is that everything going on the stack is colder than the earlier values on the stack otherwise the earlier value would be gone.
            while stack and temperatures[i] > stack[-1][0]:
                result = stack.pop()
                # we want to find the difference in days between the current day where we found the hotter and the colder day.
                res[result[1]] = i - result[1]
            # we need to keep track of both the temp and the index. also, the current day gets added into the stack no matter what.
            stack.append((temperatures[i], i))
        return res