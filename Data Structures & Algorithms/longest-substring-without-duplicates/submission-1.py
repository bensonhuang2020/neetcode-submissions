class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        left_track = 0
        for i in range(len(s)):
            while s[i] in s[left_track:i]:
                left_track += 1
            else:
                longest_length = max(longest_length, len(s[left_track:i+1]))
        return longest_length
        