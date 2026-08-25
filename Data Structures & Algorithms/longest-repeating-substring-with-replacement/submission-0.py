class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #my initial approach is that i want to do something like measuring the longest string left to right, and counting the number of differences. once differences reaches a certain #, we want to move the left pointer.
        res = 0
        left = 0
        tracked_letters = {}
        most_freq = 0
        for i in range(len(s)):
            if s[i] not in tracked_letters.keys():
                tracked_letters[s[i]] = 1
            else:
                tracked_letters[s[i]] += 1
            most_freq = max(tracked_letters.values())
            while k < ((i - left + 1) - most_freq):
                tracked_letters[s[left]] -= 1
                left += 1
            res = max(res, (i - left + 1))
        return res