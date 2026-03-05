class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = (10**9) + 7
        n = len(nums)
        total_sum = 0
        counters = [0]*(n+1)

        for start, end in requests:
            counters[start] += 1
            if end + 1 < n:
                counters[end + 1] -= 1
            
        for i in range(1, n):
            counters[i] += counters[i-1]

        nums = sorted(nums)
        counters = sorted(counters[:-1]) + [counters[-1]]
        current = 0
        for i in range(n):
            current = nums[i] * counters[i]
            total_sum += current

        return total_sum % mod
