class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # the naive solution would be to iterate through wordDict until we can find a word that fits in. we can avoid duplicate work by using a dictionary for strings and if it is end of word or if it's already seen, we mark as True.
        memo = {}
        can_break = False

        # i think this one isn't super obvious to me, but the idea is that we don't want to do duplicate work. the only time we return True is when we have no more string to work on. hence, we check the string lengths on the front, try to find it in memo from hashmap. if we don't find it, it's prob not done yet. if we find it, we return the answer whether it's true (been foudn with empty string down the line), or we return false.

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
            
            # notice that we default false here, this is so that when we send it back up, it's sent back as false.
            return False
            

        return broke(s)