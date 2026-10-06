class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # the naive solution would be to iterate through wordDict until we can find a word that fits in. we can avoid duplicate work by using a dictionary for strings and if it is end of word or if it's already seen, we mark as True.
        memo = {}
        can_break = False

        def broke(cur_string):
            if not cur_string:
                return True
            
            if cur_string in memo:
                return memo[cur_string]
            
            for word in wordDict:
                if len(word) <= len(cur_string) and word == cur_string[:len(word)]:
                    memo[cur_string] = broke(cur_string[len(word):])
                    if memo[cur_string]:
                        return True
            
            return False
            

        return broke(s)