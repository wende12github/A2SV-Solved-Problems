class Solution:
    def findValidPair(self, s: str) -> str:
        counter = Counter(s)

        for indx, val in enumerate(s):
            if indx == 0:
                continue
            if s[indx] != s[indx - 1]:
                if counter[s[indx]] == int(s[indx]) and counter[s[indx - 1]] == int(s[indx - 1]):
                    return s[indx -1: indx + 1]

        return ""
