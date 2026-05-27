class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [[-1 for _ in range(2)] for _ in range(n)]

        def recur(i, bought):
            if i >= n:
                return 0

            if memo[i][bought] != -1:
                return memo[i][bought]

            if not bought:
                buy = recur(i + 1, True) - prices[i]
                skip_buy = recur(i + 1, False)
                result = max(buy, skip_buy)
            else:
                sell = recur(i + 2, False) + prices[i]
                skip_sell = recur(i + 1, True)
                result = max(sell, skip_sell)

            memo[i][bought] = result
            return result

        return recur(0, False)