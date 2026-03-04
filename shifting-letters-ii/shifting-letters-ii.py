class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        result = [0]*(n+1)

        for start, end, dic in shifts:
            if dic == 1:
                result[start] += 1
                if end + 1 < n:
                    result[end + 1] -= 1
            else:
                result[start] -= 1
                if end + 1 < n:
                    result[end + 1] += 1

        shift = 0
        res = []
        for i, cha in enumerate(s):
            shift += result[i]
            char = chr((ord(cha) - ord("a") + shift) % 26 + ord("a"))
            res.append(char)

        return ''.join(res)
