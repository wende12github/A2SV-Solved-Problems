class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows, cols = len(image), len(image[0])

        for row in image:
            left, right = 0, len(row) - 1

            while left <= right:
                if row[left] == row[right]:
                    row[left], row[right] = row[left]^1, row[right]^1

                left += 1
                right -= 1
        return image