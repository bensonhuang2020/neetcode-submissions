class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # we need to find whether each border o can reach other o's. if they can, we can't flip those back. hence those border cells and the connected can't be surrounded but the rest are
        rows = len(board)
        cols = len(board[0])
        def capture(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            capture(r - 1, c)
            capture(r + 1, c)
            capture(r, c - 1)
            capture(r, c + 1)
        for i in range(rows):
            capture(i, 0)
            capture(i, cols - 1)
        for j in range(cols):
            capture(0, j)
            capture(rows - 1, j)
        
        for x in range(rows):
            for y in range(cols):
                # if it's still O, it wasn't changed to 'T' so it was surrounded
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                # Otherwise, it's not surrounded
                elif board[x][y] == 'T':
                    board[x][y] = 'O'
