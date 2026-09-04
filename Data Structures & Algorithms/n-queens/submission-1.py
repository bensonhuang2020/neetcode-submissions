class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # my approach would be to simulate the board, probably try to put a queen on each tile as the dfs technique, see if it works, if it does we continue. if not, we return and backtrack for each one anyways. if we hit the number of queens placed == n, append the current board layout to res.
        res = []
        board = [["."] * n for _ in range(n)]

        def is_valid(row, col):
            # this function should check that the board is able to host the piece. since our index/row is already being iterated through, there's no coincidence through this. hence we just have have to check column space + diagonals
            # let's start with columns
            for r in range(row):
                # we haven't assigned q to the current coord)
                # we have to check the same column for other rows.
                if board[r][col] == "Q":
                    return False
            
            # now let's address the diagonals, since we're going down (the rows are being built top down), we only have to check the upper-left diagonal and the upper right diagonal

            # upper-left diagonal
            r, c = row - 1, col - 1

            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            
            # upper-right diagonal
            r, c = row - 1, col + 1

            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1
            
            return True

        def dfs(i):
            # base case
            if i == n:
                res.append(["".join(row) for row in board])
                return
            for col in range(n):
                # backtracking logic since we're traversing rows, but we assign the current coord to Q if we can, backtrack after returning.
                if is_valid(i, col):
                    board[i][col] = "Q"
                    dfs(i + 1)
                    board[i][col] = "."
        
        dfs(0)
        return res
    
    
