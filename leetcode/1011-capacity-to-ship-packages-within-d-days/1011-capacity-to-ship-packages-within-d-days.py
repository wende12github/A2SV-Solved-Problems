class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        result = right

        def shipped(cap):
            day = 1
            current_cap = cap
            for w in weights:
                if current_cap - w < 0:
                    day += 1
                    current_cap = cap
                current_cap -= w

            return day <= days

        while left <= right:
            mid = (left + right) // 2

            if shipped(mid):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result