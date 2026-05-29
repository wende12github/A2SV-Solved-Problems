class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * m
        
        for i in range(1, n):
            for j in range(1, m):
                row[j] += row[j - 1]
                
        return row[-1]