class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        mini_ops = 0

        for i in range(length - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                mini_ops += 1

        if nums[-1] == 0 or nums[-2] == 0:
            return -1

        return mini_ops