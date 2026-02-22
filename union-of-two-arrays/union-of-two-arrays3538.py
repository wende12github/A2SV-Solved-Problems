class Solution:    
    def findUnion(self, a, b):
        res = set(a)
       
        n = len(b)
        
        for i in range(n):
           if b[i] not in res:
                res.add(b[i])
           
        return res
