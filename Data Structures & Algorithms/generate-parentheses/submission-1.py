class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        # the approach is that we want to backtrack, keep a stack open with results. we could also do a string but we'd have to keep storing it. if we have equal # of opened and closed, then we hit n parentheses. if the number of opened is less than n, we can get more opened. we can only match the closed to the opens, we cannot have more closed than opens.
        def parenthesis(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                parenthesis(opened + 1, closed)
                stack.pop()
            
            if closed < opened:
                stack.append(")")
                parenthesis(opened, closed + 1)
                stack.pop()
        
        parenthesis(0, 0)
        return res
            