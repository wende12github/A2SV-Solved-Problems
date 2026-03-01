class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [0]*len(s)

        for i, char in enumerate(s):
            result[indices[i]] = char
        res = ''
        
        for c in result:
            res += c
        return res
