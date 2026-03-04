class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {0: 1}
        count = 0
        current_sum = 0
        i = 0
        for num in nums:
            current_sum += num
            if current_sum - goal in prefix:
                count += prefix[current_sum - goal]
            prefix[current_sum] = prefix.get(current_sum, 0) + 1

        return count
