class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col, visited, prev):
            if ((row, col) in visited or row < 0 or col < 0 or row == rows or col == cols or heights[row][col] < prev):
                return
            
            visited.add((row, col))
            for dr, dc in dirc:
                nrow, ncol = row + dr, col + dc
                dfs(nrow, ncol, visited, heights[row][col])

        pacific, atlantic = set(), set()

        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols-1, atlantic, heights[i][cols-1])
        
        for i in range(cols):
            dfs(0, i, pacific, heights[0][i])
            dfs(rows-1, i, atlantic, heights[rows-1][i])

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])

        return result