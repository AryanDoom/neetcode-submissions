class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        return True