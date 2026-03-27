class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * (n) for i in range(n)]
        result = []
        
        def safeMove(rows, cols):
            for i in range(len(board)):
                if board[i][cols] == "Q":
                    return False
                    
                if rows - i >= 0:
                    if cols - i >= 0 and board[rows-i][cols-i] == "Q":
                        return False
                    if cols + i < len(board) and board[rows-i][cols+i] == "Q":
                        return False

            return True

        def dfsBacktrack(row):
            if row == n:
                result.append(["".join(i) for i in board])
                return

            for col in range(n):
                if safeMove(row, col):
                    board[row][col] = "Q"
                    dfsBacktrack(row + 1)
                    board[row][col] = "."

        dfsBacktrack(0)
        return result