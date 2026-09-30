class Solution:
    def climbStairs(self, n: int) -> int:
        # this is dp because we don't want to recalculate when we get the same results again. this means that when we need climb(n-1) or climb(n-2) and we've already found them, we should store to avoid redoing a lot of work. otherwise, we just run recursion until we hit the base case.
        memo = {}
        def climb(n):
            if n <= 2:
                return n
            if not memo.get(n):
                memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]
        return climb(n)