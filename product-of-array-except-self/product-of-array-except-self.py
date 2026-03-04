class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        first_pro = 1

        for i in range(n):
            result[i] = first_pro
            first_pro *= nums[i]

        second_pro = 1

        for i in range(n-1, -1, -1):
            result[i] *= second_pro
            second_pro *= nums[i]

        return result
