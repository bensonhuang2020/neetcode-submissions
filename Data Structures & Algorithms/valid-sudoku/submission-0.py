class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        boxes = defaultdict(list)

        # handle rows and 3x3
        for x in range(len(board)):
            row = set()
            for y in range(len(board[x])):
                if board[x][y] in row and board[x][y] != ".":
                    return False
                # do the 3x3
                box = (x // 3, y // 3)
                if board[x][y] in boxes[box] and board[x][y] != ".":
                    return False
                boxes[box].append(board[x][y])
                row.add(board[x][y])

        #handle the cols
        for y in range(len(board[0])):
            col = set()
            for x in range(len(board)):
                if board[x][y] in col and board[x][y] != ".":
                    return False
                col.add(board[x][y])
        


        return True
