class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))

        while left <= right:
            curr = left*left + right*right
            if curr == c:
                return True
            elif curr > c:
                right -= 1
            else:
                left += 1

        return False
            
