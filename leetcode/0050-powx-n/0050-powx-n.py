class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        
        result = self.myPow(x, abs(n) // 2)
        result *= result

        answer = 0
        if n % 2:
            answer = x*result
        else:
            answer = result
            
        if n >= 0:
            return answer
        else:
            return 1 / answer