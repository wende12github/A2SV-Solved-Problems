class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(current_index: int, current_sum: int) -> int:
            if current_index == len(nums):
                return 1 if current_sum == target else 0
            
            if (current_index, current_sum) in memo:
                return memo[(current_index, current_sum)]

            add_ways = backtrack(current_index + 1, current_sum + nums[current_index])
            sub_ways = backtrack(current_index + 1, current_sum - nums[current_index])

            memo[(current_index, current_sum)] = add_ways + sub_ways
            return memo[(current_index, current_sum)]

        return backtrack(0, 0)