class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen_fruits = {}
        res = total = l = r = 0
        while r < len(fruits):
            seen_fruits[fruits[r]] = 1 + seen_fruits.get(fruits[r], 0)
            total += 1
            while len(seen_fruits.keys()) > 2:
                seen_fruits[fruits[l]] -= 1
                total -= 1
                if seen_fruits[fruits[l]] == 0:
                    del seen_fruits[fruits[l]]
                l += 1
            r += 1
            res = max(res, total)
        return res
