class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sums = 0
        min_sum = 1

        for num in nums:
            sums += num
            min_sum = min(min_sum, sums)

        if min_sum > 0:
            return 1
        return -1*min_sum + 1
