class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)

        for cha in s:
            t.remove(cha)
            
        return t[0]