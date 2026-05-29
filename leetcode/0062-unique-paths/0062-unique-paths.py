class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0:
                    grid[0][j] = 1
                elif j == 0:
                    grid[i][j] = 1
                else:
                    up = grid[i - 1][j]
                    left = grid[i][j - 1]
                    grid[i][j] = up + left
                    
        return grid[n - 1][m - 1]