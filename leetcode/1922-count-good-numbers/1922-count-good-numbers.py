class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def helperPow(num, n):
            result = 1

            while n > 0:
                if n % 2:
                    result = (result * num) % MOD

                n = n // 2
                num = (num * num) % MOD

            return result

        even = ceil(n / 2)
        odd = n // 2

        return (helperPow(5, even) * helperPow(4, odd)) % MOD