class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_ = x
        rev = 0
        
        while num_ != 0:
            rev = rev * 10 + num_ % 10
            num_ = num_ // 10
        return rev == x
