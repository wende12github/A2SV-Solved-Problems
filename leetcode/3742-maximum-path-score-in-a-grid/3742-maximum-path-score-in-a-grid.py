class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[float('-inf')] * (k + 1) for _ in range(cols)]
        cur_k = k
        cur_score = 0
        for i, val in enumerate(grid[0]):
            cur_k -= (val > 0)
            cur_score += val
            if i == 0 and cur_k < 0: return -1
            if cur_k < 0: continue
            dp[i][cur_k] = cur_score
        for r in range(1, rows):
            new_dp = [[float('-inf')] * (k + 1) for _ in range(cols)]
            for i, val in enumerate(grid[r]):
                for j in range(k + 1):
                    new_k = j - (val > 0)
                    if new_k < 0: continue
                    new_dp[i][new_k] = max(new_dp[i][new_k], dp[i][j] + val)
                    if i > 0:
                        new_dp[i][new_k] = max(new_dp[i][new_k], new_dp[i - 1][j] + val)
            dp = new_dp
        ans = max(dp[-1])
        return ans if ans != float('-inf') else -1 