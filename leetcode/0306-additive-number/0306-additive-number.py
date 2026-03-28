class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            if i > 1 and num[0] == '0':
                break

            for j in range(i + 1, n):
                if j - i > 1 and num[i] == '0':
                    break

                num1_str = int(num[:i])
                num2_str = int(num[i:j])
                
                if self.dfsBacktrack(num1_str, num2_str, num[j:]):
                    return True
        return False

    def dfsBacktrack(self, num1, num2, reman_str):
        if not reman_str:
            return True

        exp_sum = num1 + num2
        exp_sum_str = str(exp_sum)
        
        
        if reman_str.startswith(exp_sum_str):
            return self.dfsBacktrack(num2, exp_sum, reman_str[len(exp_sum_str):])
        
        return False