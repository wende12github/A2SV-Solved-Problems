class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start, end = 0, n-1
        max_area = 0

        while start < end:
            val = end - start
            current_area = min(height[start], height[end]) * val
            max_area = max(max_area, current_area)

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return max_area
