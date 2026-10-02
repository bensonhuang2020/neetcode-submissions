class Solution:
    def countSubstrings(self, s: str) -> int:
        # same approach as other palindromic question, but instead of keeping the longest, we count every single one. start with base case of every single letter, then we expand with evens and odds.
        # i'm just keeping n as len cause it's easier to work with and i don't have to run it over and over.
        n, num_palindromes = len(s), len(s)

        # we use num_palindromes as the nonlocal, l starts from 1 for the odd because we already did the base l=0 case to start, everything else is the same
        def odd_palindrome(i):
            nonlocal num_palindromes
            l = 1
            while (i + l < n) and (i - l >= 0) and s[i - l] == s[i + l]:
                num_palindromes += 1
                l += 1

        # even still does the 0 case cause the base case isn't covered (**)
        def even_palindrome(i):
            nonlocal num_palindromes
            l = 0
            while (i + l + 1 < n) and (i - l >= 0) and s[i - l] == s[i + l + 1]:
                num_palindromes += 1
                l += 1

        for x in range(len(s)):
            odd_palindrome(x)
            even_palindrome(x)
        return num_palindromes