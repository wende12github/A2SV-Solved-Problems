class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        ans = 0
        big = 0
        found = False

        for i in range(50, -1, -1):
            curr = 1 << i

            if (a & curr) == 0 and (b & curr) == 0:
                if i < n:
                    ans += curr

            elif (a & curr) != 0 and (b & curr) == 0:
                if big == 0:
                    big = -1
                elif big == -1 and i < n:
                    ans += curr

            elif (a & curr) == 0 and (b & curr) != 0:
                if big == 0:
                    big = 1
                elif big == 1 and i < n:
                    ans += curr 

        mod = 1000000007
        a ^= ans
        b ^= ans
        a %= mod
        b %= mod
        ans = (a * b) % mod

        return ans