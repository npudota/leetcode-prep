class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r] or board[r][c] in cols[c] or board[r][c] in boxes[r//3,c//3]:
                    return False
                row[r].append(board[r][c])
                cols[c].append(board[r][c])
                boxes[r//3,c//3].append(board[r][c])
        return True
                

        


        