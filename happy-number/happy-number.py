class Solution:
    def isHappy(self, n: int) -> bool:
        visitted = set()
        
        while n not in visitted:
            visitted.add(n)
            n = self.SquareSum(n)

            if n == 1:
                return True

        return False

    def SquareSum(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit

            n = n // 10

        return output
