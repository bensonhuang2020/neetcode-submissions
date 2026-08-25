class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # guaranteed that s1 is the smaller of the 2
        if len(s1) > len(s2):
            return False
        s1_counted = Counter(s1)
        s2_window = {}
        left_track = 0
        for s in range(len(s2)):
            if not s2_window.get(s2[s]):
                s2_window[s2[s]] = 1
            else:
                s2_window[s2[s]] += 1
            if s1_counted == s2_window:
                return True
            if sum(s2_window.values()) == len(s1):
                s2_window[s2[left_track]] -= 1
                if s2_window[s2[left_track]] == 0:
                    del s2_window[s2[left_track]]
                left_track += 1
        return False


