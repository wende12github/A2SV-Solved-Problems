class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            board[row][col] = '#'

            for dr, dc in dirc:
                nrow, ncol = row + dr, col + dc
                if (nrow >= 0 and nrow < rows) and (ncol >= 0 and ncol < cols) and board[nrow][ncol] == 'O':
                    dfs(nrow, ncol)
                    
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols-1] == 'O':
                dfs(i, cols-1)
        for i in range(cols):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[rows-1][i] == 'O':
                dfs(rows-1, i)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'

        return board