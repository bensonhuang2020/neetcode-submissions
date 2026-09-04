class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # hold a set of coordinates to represent the visited spots so we don't double count
        visited = set()
        
        # set up the dfs backtrack
        def dfs(r, c, i):
            # if the length of the word is correct, we found the word
            if i == len(word):
                return True
            
            # if the minimum is less than 0, that means we're off of the board, so it's false. same if it's larger. if the word at the given index is not equal to what is on the current location on the board, we're not on the right track.
            if (min(r, c) < 0) or r >= len(board) or c >= len(board[0]) or word[i] != board[r][c] or (r, c) in visited:
                return False
            
            # we've explored the current location, so add it to the visited
            visited.add((r, c))
            # we'll visit all surrounding areas, having or makes it so that we return the result of any possible positives.
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            # then we remove the visited at the end since we're backtracking
            visited.remove((r, c))
            return res
        
        # gotta travel the whole board.
        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(x, y, 0):
                    return True
        return False