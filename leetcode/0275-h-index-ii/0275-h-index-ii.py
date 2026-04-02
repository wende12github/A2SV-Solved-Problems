class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        left, right = 0, n-1
        result = 0
        while left <= right:
            mid = (right + left) // 2

            if citations[mid] < n - mid:
                left = mid + 1
            else:
                result = n - mid
                right = mid - 1

        return result