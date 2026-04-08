class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, max(candies)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            total = 0
            for c in candies:
                total += c // mid

            if total >= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result