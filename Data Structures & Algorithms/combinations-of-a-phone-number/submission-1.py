class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {"2" : "abc", "3" : "def", "4" : "ghi", "5": "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        digit_len = len(digits) - 1
        res = []
        curr_word = []
        
        def dfs(i):
            if i > digit_len:
                return
            for x in phone_dict[digits[i]]:
                curr_word.append(x)
                if i == digit_len:
                    res.append("".join(curr_word))
                dfs(i + 1)
                curr_word.pop()
        dfs(0)
        return res
