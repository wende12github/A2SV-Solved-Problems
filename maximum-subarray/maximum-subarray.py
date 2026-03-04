class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = 0
        global_max = nums[0]

        for i in range(len(nums)):
            num = nums[i]

            current_max = max(num, current_max + num)

            if global_max < current_max:
                global_max = current_max

        return global_max
