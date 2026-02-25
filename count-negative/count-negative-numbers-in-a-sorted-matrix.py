class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)-1
        n = len(grid[0])
        j = 0
        while m >= 0 and j < n:
            if grid[m][j] >= 0:
                j += 1
            else:
                count += n - j
                m -= 1
        
        return count
