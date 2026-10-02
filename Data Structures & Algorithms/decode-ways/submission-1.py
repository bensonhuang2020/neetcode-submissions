class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        n = len(s)
        res = 0
        def dfs(i):
            # nonlocal given that modify res
            nonlocal res
            if memo.get(i):
                return memo[i]
            # base cases is that we hit the end of the string, that's 1 decoding
            if i >= n:
                return 1
            # if we find that our current single character is '0', that doesn't map to anything so 0. also the examples show that a leading '0' is not allowed, so something like '06' immediately ends.
            if s[i] == '0':
                return 0
            # all dfs(i + 1) means is that we continue to the next letter
            res = dfs(i + 1)
            # we need to make sure that there's a next character to even consider a different encoding
            if i < n - 1:
                # if we do have space, our current letter must be '1' + '0-9' (so '1' and anything else) or '2' and anything from '0-6' or it doesn't fit with the letters
                if s[i] == '1' or (s[i] == '2' and int(s[i + 1]) < 7):
                    # in that case, we consider that as a new encoding since we can interpret from the single char and the number char. we do a new call, which adds another number since when it finishes the string in the equal, it increases. 
                    res += dfs(i + 2)
            memo[i] = res
            return res

        dfs(0)
        return res
        