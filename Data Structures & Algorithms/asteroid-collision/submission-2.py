class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #let's just try a stack
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                if asteroid > 0:
                    stack.append(asteroid)
                else:
                    if stack[-1] > 0:
                        while stack and stack[-1] > 0 and abs(asteroid) > stack[-1]:
                            stack.pop()
                        else:
                            if stack and stack[-1] > 0 and abs(asteroid) == stack[-1]:
                                stack.pop()
                            elif not stack or (stack and ((stack[-1] > 0 and abs(asteroid) > stack[-1]) or stack[-1] < 0)):
                                stack.append(asteroid)
                    else:
                        stack.append(asteroid)
        return stack
                            
