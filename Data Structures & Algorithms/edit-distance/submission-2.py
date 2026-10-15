class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # for each position in the word, we're able to make 3 changes: 1. insert a char 2. delete a char 3. replace a char
        # this is not an active actoin, but can also go forward
        # how does each action affect the words?
        # adding is an action, i is index for word1, j is index for word2
        # insert: 1 + dfs(i, j+1) since we can move on to the next char for j, but for i, we technically haven't "moved" since og index letter is the same
        # delete: 1 + dfs(i + 1, j) since we move to the next char for word1 but not for word2 since it doesn't match
        # replace a char: 1 + dfs(i + 1, j + 1), both move forward since they now both match.
        # then if both chars match: just do dfs(i + 1, j + 1)
        # if we reach the end of either word, we add the difference in lengths for between the 2 to either account for the rest of the deletes or inserts. we should memoize the locations of i and j to avoid repeated work.
        m, n = len(word1), len(word2)
        memo = {}
        def edit(i, j):
            # like other dp problems with min or max amount of moves, if we've already done the work, no need to do it again.
            if (i, j) in memo:
                return memo[(i, j)]
            # if we're at the end of word2, we need to delete the rest of the letters in word1.
            if j >= n:
                return m - i

            # if we're at the end of word1, we need to insert the rest of the letters in word2
            if i >= m:
                return n - j
        
            # if the letters at this position are the same, we never want to do any changes, so just advance.
            if word1[i] == word2[j]:
                memo[(i, j)] = edit(i + 1, j + 1)
            
            # otherwise, we always add 1, then find the min between insert, delete, and replace
            else:
                memo[(i, j)] = 1 + min(edit(i, j + 1), edit(i + 1, j), edit(i + 1, j+ 1))
            return memo[(i, j)] 

        return edit(0, 0)

