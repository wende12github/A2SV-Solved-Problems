class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing_num = 1
        patchs = 0
        i = 0

        while missing_num <= n:
            if i < len(nums) and nums[i] <= missing_num:
                missing_num += nums[i]
                i += 1
            else:
                missing_num += missing_num

                patchs += 1

        return patchs