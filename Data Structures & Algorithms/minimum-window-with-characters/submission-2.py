class Solution:
    def minWindow(self, s: str, t: str) -> str:
        valid_substring = ""
        
        #create 2 counters, 1 is filled since t is suppposed to be the substring
        t_count = Counter(t)
        s_count = Counter()

        # left slides if there is a valid substring
        left_track = 0
        
        #instead of comparing counters, keep track of how many letters are valid
        valid_letters = 0
        for i in range(len(s)):
            if not s_count:
                s_count[s[i]] = 1
            else:
                s_count[s[i]] += 1

            if s_count[s[i]] == t_count[s[i]]:
                valid_letters += 1
            
            #this represents the t_count being subset of s_count
            while valid_letters == len(t_count.keys()):
                # if there hasn't been a valid substring or it's smaller, we have a new one
                if not valid_substring or ((i - left_track + 1) < len(valid_substring)):
                    valid_substring = s[left_track:i+1]
                # while there is a valid substring, slide left to right
                s_count[s[left_track]] -= 1
                # if there are fewer letters in our substrings for a specific letter, we lost a valid letter and our substring is no longer valid.
                if s_count[s[left_track]] < t_count[s[left_track]]:
                    valid_letters -= 1
                left_track += 1
        
        return valid_substring
