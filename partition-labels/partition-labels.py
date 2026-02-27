class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = right = 0

        rightmost_idx = {char: i for i, char in enumerate(s)}

        result = []
        for i, let in enumerate(s):
            right = max(right, rightmost_idx[let])
            if i == right:
                result += [right - left + 1]
                left = i + 1

        return result
