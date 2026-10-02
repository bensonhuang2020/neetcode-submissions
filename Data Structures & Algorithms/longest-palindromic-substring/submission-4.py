class Solution:
    def longestPalindrome(self, s: str) -> str:
        # i think you can simply choose from center and expand outwards. if we are doing it from odd pov, you start with a center (let's say i), and you do i - 1 and i + 1 with a while loop until it's no longer palindromic. if we are doing it from even pov, you start with 2 headed center with i and i + 1, then you expand with i - 1, i + 1 + 1, etc. important, the memoization here is keeping a global max len + what the string is.
        # because we know that len(s) is >= 1, we can set the default longest_len to 1 and the default longest_str to s[0]
        n = len(s)
        longest_len = 1
        longest_str = s[0]
        def odd_palindrome(i):
            # same for even, but we have to make longest_len and longest_str to nonlocal since we intend to modify them.
            nonlocal longest_len, longest_str
            l = 0
            # >= 0 to avoid the 0 case, then the palindrome handles itself cause if we're odd, we only check the intervals coming out 
            while (i + l < n) and (i - l >= 0) and s[i - l] == s[i + l]:
                # l * 2 is the outside, then include center
                curr_len = (l * 2) + 1
                if curr_len > longest_len:
                    longest_len = curr_len
                    # we have to add another 1 at the end since it's inclusive:exclusive
                    longest_str = s[i - l:i + l + 1]
                l += 1

        def even_palindrome(i):
            nonlocal longest_len, longest_str
            l = 0
            while (i + l + 1 < n) and (i - l >= 0) and s[i - l] == s[i + l + 1]:
                curr_len = (l * 2) + 2
                if curr_len > longest_len:
                    longest_len = curr_len
                    # same from earlier, but we're doing even so imagine center is 2 numbers. we could've done i and i - 1, but it's same deal. 
                    longest_str = s[i - l:i + l + 2]
                l += 1
        # every number can be the center (although you can technically shorten the range or end early)
        for x in range(len(s)):
            odd_palindrome(x)
            even_palindrome(x)
        return longest_str
