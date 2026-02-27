class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = zeros = result = 0

        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            result = max(result, r - left + 1 - zeros)

        if result == n:
            return result - 1
            
        return result
