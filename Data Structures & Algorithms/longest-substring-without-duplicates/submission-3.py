class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        # sliding window
        left_track = 0

        # holds the unique substring, faster lookup than a list
        char_set = set()
        for i in range(len(s)):
            # keep removing left side until we lose the dupe
            while s[i] in char_set:
                char_set.remove(s[left_track])
                left_track += 1
            #after dupe is gone, we have to add the right side no matter what
            char_set.add(s[i])
            longest_length = max(longest_length, len(char_set))
        return longest_length
        