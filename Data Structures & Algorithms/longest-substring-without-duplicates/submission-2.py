class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        left_track = 0
        char_set = set()
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[left_track])
                left_track += 1
            else:
                char_set.add(s[i])
                longest_length = max(longest_length, len(char_set))
        return longest_length
        