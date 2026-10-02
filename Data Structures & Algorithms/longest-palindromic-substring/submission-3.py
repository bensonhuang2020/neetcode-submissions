class Solution:
    def longestPalindrome(self, s: str) -> str:
        # i think you can simply choose from center and expand outwards. if we are doing it from odd pov, you start with a center (let's say i), and you do i - 1 and i + 1 with a while loop until it's no longer palindromic. if we are doing it from even pov, you start with 2 headed center with i and i + 1, then you expand with i - 1, i + 1 + 1, etc. important, the memoization here is keeping a global max len + what the string is.
        n = len(s)
        longest_len = 1
        longest_str = s[0]
        def odd_palindrome(i):
            nonlocal longest_len, longest_str
            l = 0
            while (i + l < n) and (i - l >= 0) and s[i - l] == s[i + l]:
                curr_len = (l * 2) + 1
                if curr_len > longest_len:
                    longest_len = curr_len
                    longest_str = s[i - l:i + l + 1]
                l += 1

        def even_palindrome(i):
            nonlocal longest_len, longest_str
            l = 0
            while (i + l + 1 < n) and (i - l >= 0) and s[i - l] == s[i + l + 1]:
                curr_len = (l * 2) + 2
                if curr_len > longest_len:
                    longest_len = curr_len
                    longest_str = s[i - l:i + l + 2]
                l += 1
        for x in range(len(s)):
            odd_palindrome(x)
            even_palindrome(x)
        return longest_str
