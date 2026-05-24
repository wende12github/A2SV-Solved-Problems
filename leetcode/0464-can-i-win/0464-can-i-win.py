class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
            
        memo = {}
        
        def can_win(mask, current_total):
            if mask in memo:
                return memo[mask]
            
            for i in range(maxChoosableInteger):
                if not (mask & (1 << i)):
                    if current_total + (i + 1) >= desiredTotal:
                        memo[mask] = True
                        return True
                    
                    if not can_win(mask | (1 << i), current_total + (i + 1)):
                        memo[mask] = True
                        return True
            
            memo[mask] = False
            return False
            
        return can_win(0, 0)