class Solution:
    def isHappy(self, n: int) -> bool:
        # what are the cases that we get a loop?
        if n == 1:
            return True
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            run = 0
            new_num = n
            while new_num:
                run += (new_num % 10) ** 2
                new_num = new_num // 10

            n = run
        return True