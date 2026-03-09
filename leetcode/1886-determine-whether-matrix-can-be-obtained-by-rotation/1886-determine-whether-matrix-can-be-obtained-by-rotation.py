class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rows = len(mat)
        cols = len(mat[0])

        for _ in range(4):
            for r in range(rows):
                for c in range(r, cols):
                    mat[r][c], mat[c][r] = mat[c][r], mat[r][c]

            for row in mat:
                row.reverse()

            if mat == target:
                return True

        return False