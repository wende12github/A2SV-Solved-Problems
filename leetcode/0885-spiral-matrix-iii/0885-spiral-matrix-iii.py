class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        diractions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        result = []
        track = 0
        steps = 1
        row, col = rStart, cStart

        while len(result) < rows*cols:
            for _ in range(2):
                dr, dc = diractions[track]
                for _ in range(steps):
                    if 0 <= row < rows and 0 <= col < cols:
                        result.append([row, col])

                    row, col = row + dr, col + dc
                track = (track + 1) % 4
            steps += 1

        return result