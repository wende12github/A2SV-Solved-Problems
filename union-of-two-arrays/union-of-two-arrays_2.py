class Solution:    
    def findUnion(self, a, b):
        res = set()
        
        for i in a:
            res.add(i)
        for i in b:
            res.add(i)
           
        return res
