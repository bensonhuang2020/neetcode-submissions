class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed  = ""
        for strs in s.lower():
            if strs.isalpha() or strs.isdigit():
                trimmed += strs
        l, r = 0, len(trimmed) - 1
        while l < r:
            if trimmed[l] != trimmed[r]:
                return False
            l += 1
            r -= 1
        return True