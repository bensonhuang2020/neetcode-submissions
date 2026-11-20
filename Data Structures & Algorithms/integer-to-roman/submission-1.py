class Solution:
    def intToRoman(self, num: int) -> str:
        # essentially, we want to go through the list of possible integer lists, then get the counts by floor diving on the biggest greedy number. after a div, do a modulo to get the next number to work with.
        res = ""
        symbols = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        for symbol, val in reversed(symbols):
            count = num // val
            if count:
                res += symbol * count
                num %= val
        return res
