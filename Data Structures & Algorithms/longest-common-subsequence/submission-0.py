class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # naïve solution would be to go through with a helper function that takes the max of each subsequence, should take the max, each iteration should check that we remove a specific letter through for loops whereby we loop through the entire word and compare.

        # solution that ended up working: start from the beginning of the word index wise, we get 0 if we hit the end of either string since there's nothing to compare with. if the initial char is the same, we move both strings forward since we take the char from both strings (greedily since there's no scenario that we don't take the first char in that case). afterwards, in order to progress, we either don't take the first char of text1 or of text2. this is represented by advancing the index for either string by 1. find the max of such case.
        m, n = len(text1), len(text2)
        memo = {}

        def subsequence(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i >= m or j >= n:
                return 0

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + subsequence(i + 1, j + 1)
            
            else:
                memo[(i, j)] = max(subsequence(i + 1, j), subsequence(i, j + 1))
            return memo[(i, j)]

        return subsequence(0, 0)
            