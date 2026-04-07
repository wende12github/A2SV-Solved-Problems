class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (2 ** (n - 1))
        if k > total:
            return ''

        result = []
        def dfsBacktrack(char):
            if len(char) == n:
                result.append(char)
                return

            for c in "abc":
                if not char or char[-1] != c:
                    dfsBacktrack(char + c)

        dfsBacktrack('')
        return result[k-1]