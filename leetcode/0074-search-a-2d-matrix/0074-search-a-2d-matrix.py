class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] < target and matrix[m][-1] > target:
                break
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        row = (l + r) // 2
        left = 0
        right = len(matrix[row]) -1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False