class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
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
            