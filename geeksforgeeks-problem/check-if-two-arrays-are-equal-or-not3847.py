class Solution:
    def checkEqual(self, a, b) -> bool:
        counter = {}
        
        for i in a:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        for i in b:
            if i not in counter or counter[i] == 0:
                return False
            counter[i] -= 1
            
        return True
