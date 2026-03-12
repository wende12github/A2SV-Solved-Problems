class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        stack = []
        left, right = [-1]*length, [length]*length

        for i in range(length):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()
        for i in range(length-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            right[i] = stack[-1] if stack else length
            stack.append(i)

        max_area = 0
        for i in range(length):
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)

        return max_area